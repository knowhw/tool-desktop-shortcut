import collections
import os
import xml.etree.ElementTree as ET
from json import loads
import urllib.request 


appname=''
# glob.appname


items=[]
# glob.items

path=''
# glob.path

appdir='/usr/share/applications'

class index:
	pass

entry='Desktop Entry'
# glob.entry

action='Desktop Action'
# glob.action

puff=''
# glob.puff


context = []
insert=context.insert
extend=context.extend
push=context.append


# uptobottom=False
# glob.uptobottom


import os
LANGUAGE=os.getenv("LANGUAGE")
# glob.LANGUAGE

class select:
	base = ''
	# glob.select.base

content=''
# glob.content

_,path='{http://www.w3.org/XML/1998/namespace}lang',os.path.join(os.path.dirname(__file__), 'lang.xml')
lang=ET.parse(path)
def head(base):
	return { index for index, item in enumerate(puff) if base in item }
	
