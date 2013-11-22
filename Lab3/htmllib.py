#!/usr/local/bin/python3
# Douglas Putnam
# htmllib.py
# July, 2011

import cgi
def html5_template(title="CHANGE THE TITLE",body='<!-- content goes here -->'):
    """A function that provides a simple HTML5 template"""
    f = open('html5_template.html')
    print(f.read() % (title,body))

def html_source_code(filename):
    """Grabs a code files and presents is as source code"""
    f = open(filename, 'r')
    code = f.readlines()
    source_html = '<ol>'

    for line in code:
        got_it = ''
        if line == '\n':
            got_it = '\n'
        source_html += '<li>' + cgi.escape(line.rstrip()) + got_it + "</li>\n"

    return '<h1>File: ' + filename + '</h1>' + source_html + '</ol>'

def print_source_code(filenames):
    if isinstance(filenames,str):
        filenames = [filenames]
    """Takes a list of file names and creates a source code listing. CSS
    included"""
    source_code = []
    for i in filenames:
        source_code.append(html_source_code(i))
    print("""
<style type="text/css">
   body {font-size:10pt;} .source {background-color:#ffe;padding:1em;}
          ol li {margin:0;padding:0;line-height:120%;letter-spacing:0.015em;
          font-size:.95em; font-family:Consolas,monospace;white-space:pre}
          li::before {content: ' ';white-space:pre;} #source-code-hr { margin:6px 0;color:#ccc}
          .source-container { margin:12px 6em;padding:12px;background-color:white;}
          </style>
""")
    print('''<hr id="source-code-hr"><div class="source-container"><h1>Source Code
          for <span style="font-weight:normal;font-family:monospace;color:#333">{}</span></h1>'''.format(", ".join(filenames)))
    for i in source_code:
        print("""
<div class="source">
{}
</div>
""".format(i))
    print('</div>')

def content_type(type='text/html'):
    print('Content-type: {}\n'.format(type))

# testing
if __name__ == '__main__':
    html5_template('this is an example')
    html5_template('this is an example','this is the body')
    print_source_code([__file__])
