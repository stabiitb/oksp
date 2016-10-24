import os
from datetime import datetime
from wsgiref.util import FileWrapper

from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.encoding import smart_str

from .forms import DocUploadForm
from .htmlify import HTMLifier
from .models import Documentation

DOC_DIR = os.path.abspath(os.path.dirname(__name__)) + '/docupload/docs/'


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
    html = HTMLifier(doc_base_path=DOC_DIR)
    text = request.GET.get('text')
    title = request.GET.get('title')
    description = request.GET.get('description')
    if text and title:
        #Save this file
        myfile = ContentFile(bytes(text, 'utf-8'))
        myfile.name = title
        filename, ext = html.convert(myfile)
        doc = Documentation(name=title,
                            doc_file=filename,
                            description=description,
                            pub_date=datetime.now(),
                            extension=ext)
        doc.save()
        return HttpResponseRedirect('/doc/')

    return render(request, "docupload/markdown.html")

def wysiwyg_editor(request):
    html = HTMLifier(doc_base_path=DOC_DIR)
    description = request.GET.get('description')
    text = request.GET.get('text')
    title = request.GET.get('title')
    if text and title:
        #Save this file
        myfile = ContentFile(bytes(text, 'utf-8'))
        myfile.name = title
        filename, ext = html.convert(myfile)
        doc = Documentation(name=title,
                            doc_file=filename,
                            description=description,
                            pub_date=datetime.now(),
                            extension=ext)
        doc.save()
        return HttpResponseRedirect('/doc/')

    return render(request, "docupload/wysiwyg.html")

def upload(request): 
    '''View for /doc/upload/'''

    html = HTMLifier(doc_base_path=DOC_DIR)

    if request.method == 'POST':
        form = DocUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            filename, ext = html.convert(request.FILES['doc_file'])
            doc = Documentation(name=request.POST['name'],
                                description=request.POST['description'],
                                doc_file=filename,
                                pub_date=datetime.now(),
                                extension=ext)
            doc.save()
    return HttpResponseRedirect('/doc/')


def display(request, doc_id):
    '''View for /doc/<doc_id>/'''

    db_doc = Documentation.objects.filter(id=doc_id)[0]
    ext = str(db_doc.doc_file).split('.')[-1]
    if ext == 'pdf':
        file = open('docupload/docs/' + str(db_doc.doc_file), 'r+b')
        file.seek(0)
        pdf = file.read()
        file.close()
        return HttpResponse(pdf, 'application/pdf')
    else:
        with open('docupload/docs/' + str(db_doc.doc_file)) as doc:
            return HttpResponse(doc)

def download_original(request, doc_id):
    '''View for doc/original/<doc_id>/'''

    db_doc = Documentation.objects.filter(id=doc_id)[0]
    ext = db_doc.extension
    filename = str(db_doc.doc_file).split('.')[0]
    full_filename = filename + '.' + ext
    file = open('docupload/docs/' + full_filename, 'r+b')
    response = HttpResponse(FileWrapper(file), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(full_filename)
    return response
