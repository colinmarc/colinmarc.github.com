import sys
import os
import codecs
from markdown2 import markdown

with codecs.open('base.tmpl', encoding='UTF-8') as tmplfile:
	template = tmplfile.read()

def makefile(path):
	with codecs.open(path, encoding='UTF-8') as mdfile:
		md = mdfile.read()
	
	html = template.replace(u'$content', markdown(md))
	basename = os.path.basename(path).split('.')[0]
	fname = basename + '.html'
		
	with codecs.open(fname, encoding='UTF-8', mode='w') as out:
		
		out.write(html)
		
if __name__ == '__main__':
	files = sys.argv[1:]
	for f in files: 
		makefile(f)
		
