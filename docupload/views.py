import os

from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import DocUploadForm
from .htmlify import HTMLifier
from .models import Documentation

DOC_DIR = os.path.abspath(os.path.dirname(__name__)) + "/docupload/docs/"


def index(request):
    '''View for /doc/'''

    doc_list = Documentation.objects.all()
    template = loader.get_template('docupload/index.html')
    form = DocUploadForm()

    context = {
        'doc_list': doc_list,
        'form': form,
    }
    return render(request,"docupload/index.html", context)

def editor_choice(request):
    return render(request, "docupload/editor_choice.html")

def markdown_editor(request):
    return render(request, "docupload/markdown.html")

def wsyiwyg_editor(request):
    return render(request, "docupload/wsyiwyg.html")

def upload(request): 
    '''View for /doc/upload/'''

    html = HTMLifier(doc_base_path=DOC_DIR)

    if request.method == 'POST':
        form = DocUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            filename = html.convert(request.FILES['doc_file'])
            doc = Documentation(name=request.POST['name'],
                                doc_file=filename,
                                pub_date=datetime.now())
            doc.save()
    return HttpResponseRedirect('/doc/')


def display(request, doc_id):
    '''View for /doc/<doc_id>/'''

    db_doc = Documentation.objects.filter(id=doc_id)[0]

    with open('docupload/docs/' + db_doc.doc_file) as doc:
        return HttpResponse(doc)

