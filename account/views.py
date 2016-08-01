from django.contrib import auth
from django.core.checks import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from account.models import *
from hacker_news.models import Vote
from oksp.settings.local import *
import base64
import requests
import json


def login(request):
    return HttpResponseRedirect(sso_url())


def sso_url():
    return 'https://gymkhana.iitb.ac.in/sso/oauth/authorize/?client_id='+clientid+'&response_type=' \
            'code&scope=basic%20profile%20ldap%20sex%20picture%20phone%20insti_address%20program%20secondary_emails' \
            '&redirect_uri='+redirecturl+'&state=signin'


def logout(request):
    user = request.user
    if user is not None and user.is_active:
        current_user = Member.objects.get(user=user)
        url = 'https://gymkhana.iitb.ac.in/sso/oauth/revoke_token/'
        header = {
            'Host': 'gymkhana.iitb.ac.in',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        payload = {
            'token': current_user.access_token,
            'client_id': clientid,
            'client_secret': clientsecret,
        }
        requests.post(url, data=payload, headers=header, verify=False)
        auth.logout(request)
        return redirect(reverse("hacker-news:news_list"))
    return redirect(reverse("hacker-news:news_list"))


def signup(userdata, access_token):
    username = userdata.get('username')
    first_name = userdata.get('first_name')
    last_name = userdata.get('last_name')
    email = userdata.get('email')
    roll_number = userdata.get('roll_number')
    profile_picture = userdata.get('profile_picture')
    sex = userdata.get('sex')
    contact = userdata.get('mobile')
    program = userdata.get('program')
    discipline = None
    join_year = None
    graduation_year = None
    degree = None
    if program is not None:
        discipline = program.get('department_name')
        join_year = program.get('join_year')
        graduation_year = program.get('graduation_year')
        degree = program.get('degree_name')
    address = userdata.get('insti_address')
    hostel = None
    room = None
    if address is not None:
        hostel = address.get('hostel_name')
        room = address.get('room')
    current_log = None
    secondary_emails = userdata.get("secondary_emails")
    secondary_email = None
    if secondary_emails is not None:
        if len(secondary_emails) > 0:
            secondary_email = secondary_emails[0].get('email')

    auth_user = User.objects.create_user(username=username,
                                         password=password,
                                         email=email,
                                         first_name=first_name,
                                         last_name=last_name)
    auth_user.save()

    _user = Member(user=auth_user,
                   roll=roll_number,
                   sex=sex,
                   contact=contact,
                   hostel=hostel,
                   room=room,
                   discipline=discipline,
                   join_year=join_year,
                   graduation_year=graduation_year,
                   degree=degree,
                   current_log=current_log,
                   secondary_email=secondary_email,
                   password=None,
                   profile_picture=profile_picture,
                   access_token=access_token)
    _user.save()

    _vote = Vote(user=_user)

    _vote.save()
    return


def redirect_function(request):
    authcode = request.GET.get('code', 'error')
    authtoken = (clientid + ':' + clientsecret).encode('ascii')
    authtoken = base64.b64encode(authtoken)
    url = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
    header = {
        'Host': 'gymkhana.iitb.ac.in',
        'Authorization': 'Basic ' + authtoken.decode('ascii'),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    payload = {
        'code': authcode,
        'redirect_uri': redirecturl,
        'grant_type': "authorization_code"
    }
    r = requests.post(url, data=payload, headers=header, verify=False)

    parsed_json = json.loads(r.content.decode('ascii'))
    print(parsed_json)
    access_token = parsed_json['access_token']
    userdata = getdata(access_token)
    check, data = check_enough_information(userdata)
    if not check:
        messages.Warning(
            request, "Not enough Information provided. "
            "Please allow application to access the required information.")
        return redirect(reverse("hacker-news:news_list"))

    username = userdata.get('username')
    user = User.objects.filter(username=username)

    if Member.objects.filter(user=user).exists():
        current_user = Member.objects.get(user=user)
        current_user.access_token = access_token
        current_user.save(update_fields=["access_token"])
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return HttpResponseRedirect(reverse('hacker-news:news_list'))
    else:
        signup(userdata, access_token)
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return HttpResponseRedirect(reverse('hacker-news:news_list'))


def check_enough_information(userdata):
    username = userdata.get('username')
    first_name = userdata.get('first_name')
    last_name = userdata.get('last_name')
    email = userdata.get('email')
    roll_number = userdata.get('roll_number')
    not_given_info = []
    if username is None:
        not_given_info.append('username')
    if first_name is None:
        not_given_info.append('first_name')
    if last_name is None:
        not_given_info.append('last_name')
    if email is None:
        not_given_info.append('email')
    if roll_number is None:
        not_given_info.append('roll_number')
    if len(not_given_info) > 0:
        return False, not_given_info
    return True, not_given_info


def getdata(account_token):
    fields = 'first_name,last_name,type,profile_picture,sex,username,email,program,contacts,insti_address,' \
             'secondary_emails,mobile,roll_number'
    url = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=' + fields
    header = {
        'GET /sso/user/api/user/ HTTP/1.1'
        'Host': 'gymkhana.iitb.ac.in',
        'Authorization': 'Bearer ' + account_token
    }
    r = requests.get(url, headers=header, verify=False)
    parsed_json = json.loads(r.content.decode('ascii'))
    return parsed_json
