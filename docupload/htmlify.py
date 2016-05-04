'''
HTMLify: Convert any fileformat supported by pandoc to HTML5
'''

import os
import pypandoc


def get_html(doc_file):
    '''Uses pypandoc to convert uploaded file to HTML5'''

    tmp_loc = '/tmp/uploaded_' + str(doc_file)

    with open(tmp_loc, 'wb') as tmp_file:
        for chunk in doc_file.chunks():
            tmp_file.write(chunk)
    html = pypandoc.convert(tmp_loc, 'html5')
    os.remove(tmp_loc)

    return html


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

        html = get_html(doc_file)

        with open(doc_dir + file_name + '.html', 'wb') as doc_stored:
            doc_stored.write(bytes(html, 'utf-8'))

        return file_name + '.html'
