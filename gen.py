import sys
import os
from markdown2 import markdown

HEADER = """
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<link href='http://fonts.googleapis.com/css?family=Buenard:400,700' rel='stylesheet' type='text/css'>
<link href="styles.css" rel="stylesheet"></link>

"""

def open_md_file(path):
	with open(path, 'r') as mdfile:
		md = mdfile.read()
	
	html = HEADER + markdown(md)
	basename = os.path.basename(path).split('.')[0]
	fname = basename + '.html'
		
	with open(fname, 'w') as out:
		out.write(html.encode('utf8'))
		
if __name__ == '__main__':
	files = sys.argv[1:]
	for f in files: 
		open_md_file(f)
		
