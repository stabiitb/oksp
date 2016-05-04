'''
HTMLify: Convert any docx/md/tex file to HTML
'''

import subprocess

import markdown2
from pydocx import PyDocX

def doc_convert(doc_file):
    '''Uses PyDocX to convert docx file'''

    return PyDocX.to_html(doc_file)

def md_convert(doc_file):
    '''Uses markdown2 to convert markdown file'''

    tmp_loc = '/tmp/md_uploaded.md'

    with open(tmp_loc, 'wb') as tmp_file:
        for chunk in doc_file.chunks():
            tmp_file.write(chunk)

    return markdown2.markdown_path(tmp_loc)

def tex_convert(doc_file):
    '''Uses TtH executable to convert TeX/LaTeX file'''

    tmp_loc = '/tmp/tex_uploaded.tex'

    with open(tmp_loc, 'wb') as tmp_file:
        for chunk in doc_file.chunks():
            tmp_file.write(chunk)

    with open(tmp_loc, 'rb') as tmp_file:
        p = subprocess.Popen(["tth"], stdin=tmp_file, stdout=subprocess.PIPE)
        out = p.communicate()[0]

        return str(out, 'utf-8')

class HTMLifier():
    '''
    HTMLifier: Class which handles conversion of any docx/md/tex file to HTML
    '''


    def __init__(self, doc_base_path='.'):
        self.doc_base_path = doc_base_path

    def convert(self, doc_file):
        '''Middleware function to interface with different <format>_convert functions'''

        file_name = str(doc_file)
        ext = file_name.split('.')[-1]
        file_name = file_name[:len(file_name) - len(ext) - 1]
        doc_dir = self.doc_base_path
        html = ''
        if ext[:3] == 'doc':
            html = doc_convert(doc_file)
        elif ext in ('md', 'markdown'):
            html = md_convert(doc_file)
        elif ext in ('tex', 'latex'):
            html = tex_convert(doc_file)

        with open(doc_dir + file_name + '.html', 'wb') as doc_stored:
            doc_stored.write(bytes(html, 'utf-8'))
