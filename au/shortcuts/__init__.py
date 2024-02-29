


# from au.desktop import export
import au.temp

from au.listdir import applications
from au.shortcuts import glob

# import multiprocessing


class test:	
	
	# head = 0
	
	def __translate(head, base, key, value, action_key=None):
		# Wed Feb 28 20:05:17 CST 2024
		
		for to in [ item.get(glob._) 
					for item in glob.lang.findall('name') 
					if item.get(glob._) ]: 
			
			

			googleapis = "/translate_a/single?client=gtx&dt=t&"
			query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, to, value)
		
	
			if not [ item for item in glob.context if item [0:4] == [ base, None, to, key ] ]:
				head+=1
				glob.insert( head-1, [ "%s" % base, None if base == glob.entry else action_key , to, key, glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0] ])
		
				
	def group(key, value, base, action_key=None):
		# test.group(key, value, desk.action, action_key)
		
		base = getattr(glob, base.__name__)
		
	
		
		if base == glob.entry:
			
		
			index = [  index  for index, item in enumerate(glob.context )
			if item [0] ==   "%s" % base  and item [3] == key ] 
			
			head, tail = index [0], index [-1] if index else None
			# __translate(head, base, key, value)
			
			test.__translate(head, base, key, value)
			

			
		elif base == glob.action:
		
		
			
			index = [  index  for index, item in enumerate(glob.context )
			if item and item [0] == "%s" % base  and item [3] == key ] 
			
			head, tail = index [0], index [-1] if index else None
			
			test.__translate(head, base, key, value, action_key)
			
	
				
		return glob
		"""

		
		"""
		
	def index_tail(base):
		
		
		return [ index -1 for index in range(glob.context.index([ base ]+ [None] * 4), len(glob.context)) 
		if not base in glob.context [index] ][-1]
		# action icin calismayabilir
		

	def string(key=None, value=None, base=None, index=None, action=None):
		
		if action:
			
			action = "%s %s" % (glob.action, action)
			
			
			if not index:
				
				
				base = [action, None, None, None]
				# base: Desktop Action test None None None
				glob.extend([base, ["%s" % action, glob.LANGUAGE, key, value]])
				# base yok
			else:

				
				exists = [ index for index, item in enumerate(glob.context) 
				if action  == item [0] and item[2] == key ]
				# base var mi?
				
				
				
				if exists:
					glob.context [exists [0]] [-1] = value
					# base var, key var
				else:

					# head, tail = min(index), max(index)
					glob.insert(min(index)+1, [action, glob.LANGUAGE, key, value])
					# base var key yok
					
				
		else:
			
			if not index is not None:

				#for index in range(glob.context.index([ glob.entry ]+ [None] * 4), 100):
					# max one double zero lines
					
				#	if not glob.entry in glob.context[index]:
				#		index = index -1
				#		break
				tail = test.index_tail(glob.entry)
				
				glob.context.insert(tail, [ glob.entry, None, glob.LANGUAGE, key, value ] )
				# ['Desktop Entry', None, 'en_US', 'Exec', '/usr/share/myapp/test']

				""" not found key """
				
			else:
				

				glob.context[index][-1] = value
				""" found key """
				
				
		return test
	def file_update():
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					test.content+= "[%s]\n" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							test.content+= "%s=%s\n" % (key, value)
					else: 
						test.content+= "%s[%s]=%s\n" % (key, lang, value)

		tempfile, name = au.temp.filetouch(test.content)
		tempfile.pkexec.mv2(glob.path)
		
		return glob
		

class desktop:

	def path(name):
		
		listdir = applications()
		""" usr/share/applications """
		
		return listdir.get(name)
		
		

		
class desk:
	
	# content = ""
	
	class entry:
		
		def getindex(key):
			try:
				return [ index for index, item in enumerate(glob.context) 
				if ["%s" % glob.entry, None, glob.LANGUAGE, key] == item [0:4] ] [0]
				""" group disinda kalan """
			except:
				return None
				
		
		def group(key, value):
			
			
			
			return test.group(key, value, desk.entry)
			
			# export.test.group(key, value, desk.entry)
			# key, value, base=None, index=None, action=None


		def set(key=None, value=None):
		
            
			index = desk.entry.getindex(key)
			return test.string(key=key, value=value, index=index)
			
			# export.test.string(key=key, value=value, index=index)
			# key, value, base=None, index=None, action=None
			# glob.context
	
			return glob
			
		def add(key, value):
			return desk.entry.set(key, value)
		def pop(key):
			
			index = [ index for index, item in enumerate(glob.context) 
			if item and glob.entry == item [0] and key == item [-2]  ]
			# ['Desktop Entry', None, 'en_US', 'Version', '1.0'], [], []
			# defactoring: and not item
			# sugar: soldan saga dogru calisiyor
			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				

			return glob
			
		def remove(key):
			return desk.entry.pop(key)
			
		def get(key):
			
			
			getext =  [ item for item in glob.context 
			if ["%s" % glob.entry, None, glob.LANGUAGE, key] == item [0:4]] 
			# ['Desktop Entry', 'en_US', 'Icon', 'bix']
			
			if getext:
			
				base, base_key, lang, key, value = getext [0]  if getext else [None]*4
				# [None]*4 -> defactoring
				# when not found key
			
				return value
		
			
	class action:
		
		def __getindex(action):
			# Mon Feb 19 08:03:03 CST 2024
			
			try:
				return [ index for index, item in enumerate(glob.context) 
			if "%s %s" % (glob.action, action)  == item [0] ]
			except:
				return None
				# action: defactoring
				
		def group(key, value, action_key):
			#(key, value, action_key)
			
			return test.group(key, value, desk.action, action_key)
			
			# export.test.group(key, value, desk.action)
			# key, value, base=None, index=None, action=None
			
			
		def set(key, value, action):
			index = desk.action.__getindex(action)
		
			return test.string(key, value, base=None, index=index, action=action)
			# export.test.string(key, value, base=None, index=index, action=action)
			
			"""
			
			[Desktop Entry]
			Exec=/usr/share/myapp/test
			Name=myapp
			Icon=face-heart

			
			"""
			
			return glob
			
		def add(key, value, action):
			return desk.action.set(key, value, action)

		def pop(key):
			
			index = [ index for index, item in enumerate(glob.context) 
			if item and glob.action == item [0] and key == item [-2]  ]
			# ['Desktop Entry', None, 'en_US', 'Version', '1.0'], [], []
			# defactoring: and not item
			# sugar: soldan saga dogru calisiyor
			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				

			return glob
		def popitem(key):
			return desk.action.pop(key)
			
		def get(key, action_key):
			# esk.action.get("Name", action_key="X")
			
			
			getext =  [ item for item in glob.context 
			if item and ["%s" % glob.action, action_key, glob.LANGUAGE, key] == item [0:4]] 
			# ['Desktop Action test', 'en_US', 'Icon', 'geany']
			
			
			
			
			return getext [0][-1] if getext else None
class getitem:

		
	def __setitem__(self, key,value):
		desk.entry.set(key=key, value=value) 
class Base:
	Entry = getitem()
	
	entry = desk.entry
	action = desk.action
	

	def update_file():
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					test.content+= "[%s]\n" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							test.content+= "%s=%s\n" % (key, value)
					else: 
						test.content+= "%s[%s]=%s\n" % (key, lang, value)

		tempfile, name = au.temp.filetouch(test.content)
		tempfile.pkexec.mv2(glob.path)
		
		return glob
	
	# def set():
	#	for key, value in Base.Entry.items():
	#		desk.entry.set(key=key, value=value)
	#	return export.test
		
def create():
	""" calisma klasorunde kisayol olustur """

def __getitems(line):
	
	
	key, val = line.split(chr(61))
	
	if chr(91) in key :
		return [ key [key.index(chr(91))+1: key.index(chr(93)) ], key [0: key.index(chr(91))], val ] 
		# ['tr', 'Name', 'bix']
	else:
		return [ glob.LANGUAGE, key, val ]
		# ['en_US', 'Categories', 'GTK;GNOME;Utility;']

def content(name):
	
	
	glob.path = desktop.path(name) 
	
	# solution
	del glob.context [:]
	
	
	
	#glob.index.action = None
	# varsayilan baslangic degerleri
	
	
	for line in open(glob.path):
		
		line = line.strip()
		
		
		if line:
		
		
			if line.startswith("#"):
				continue
			
			else:
			
				if line.startswith(chr(91)):
					
					item = chr(32).join(line [1: line.index(chr(93))].split())
					# Desktop Entry
					
					if item != glob.entry:
						x = item.split() 
						
						glob.select=chr(32).join(x[0:2])
						basekey = x [-1]
					else:
						glob.select=item
					
					glob.context.append([glob.select]+[None]*4)
					# Desktop Action
					
					
				else:
					
					item = __getitems(line)
					glob.context.append([glob.select]+[None if glob.select == glob.entry else basekey]+item)
					# 'Desktop Entry', None, 'en_US', 'Name', 'test'
					
	return Base			
	
	
def print_file():
	
	for items in glob.context:
	
		if items:
			# defactoring
			
			base, action_key, lang, key, value = items
			
			
			if action_key:
				

				if not "[%s %s]" % (base, action_key) in glob.content:
					glob.content += "[%s %s]\n" % (base, action_key)
				
				if lang == glob.LANGUAGE:
					glob.content += "%s=%s\n" % (key, value)
				else:
					glob.content += "%s[%s]=%s\n" % (key, lang, value)
				
				
			
			else:
				if items [1:] == [None] * 4:
					
					if base == glob.action:
						continue
					else:
					
						glob.content += "[%s]\n" % base

				else:
					if lang == glob.LANGUAGE:
						glob.content += "%s=%s\n" % (key, value)
					else:
						glob.content += "%s[%s]=%s\n" % (key, lang, value)
						
	return glob.content
	# Wed Feb 28 21:13:50 CST 2024

	
	
	
	
	
	
	
	
	
	
	
	
	
	
