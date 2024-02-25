

# from au.desktop import export
import au.temp

from au.listdir import applications
from au.desktop import glob




class test:	
	
	content = ""
	
	
	def print_file():
		
		arr = []
		
		"""
		
		[Desktop Entry]
		
		Name=Test
		Exec=/usr/share/test/test
		Icon=geany
		Type=Application
		Categories=Network;InstantMessaging;
		Path=/usr/bin
		
		[Desktop Action X]
		Name=test
		
		"""
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					yield "[%s]" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							yield "%s=%s" % (key, value)
					else: yield "%s[%s]=%s" % (key, lang, value)
				
	def group(key, value, base):
		
		
		base = getattr(glob, base.__name__)
		
		
		gl = [  item  for item in glob.context 
		if item [0:3] == [ base, glob.LANGUAGE, key ] ]
		# glob.LANGUAGE isExists
		
		
		
		if not gl: glob.insert( glob.index.entry+1, [ base, glob.LANGUAGE, key, value ])
		# glob.LANGUAGE not Exists
		
		"""
		
		[Desktop Entry]
		Exec=/usr/share/test/test
		Name=test
		Icon=face-heart

		
		"""
	
		
		index = [  index for index, item in enumerate(glob.context) 
		if  item [0] == base and item [1] == glob.LANGUAGE and item [2] == key ] [0]
		# index: gl.index


		
		langs = [ item.get(glob._) 
		for item in glob.lang.findall('name') 
		if item.get(glob._) ]
		

		for lang in langs: 
			
			# 132 world languages
			
			"""
			
			[mk]=test
			[hi]=test
			[lb]=test
			[lg]=test
			[lt]=test
			[ln]=test
			[lv]=test
			[la]=test
			[lo]=test
			[ky]=test
			
			..
			..
			..
			
			"""
			
			items = [  item for item in glob.context 
			if item [0:3] == [ base, lang, key ] ]
			
			
			if not items:
					
				googleapis = "/translate_a/single?client=gtx&dt=t&"
				query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s" % (googleapis, lang, value)
				
				res = glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0]
				# res: value
				
				print(lang, key, res)
				
				glob.insert( index, [ base, lang, key, res ])
				

				
		return test

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
				items = glob.entry, glob.LANGUAGE, key, value
				
				glob.context.insert(glob.index.entry + 1, list(items) )
				# tuple: [['Desktop Entry', None, None, None], ('Desktop Entry', 'en_US', 'Name', 'myapp')]
				# list: defactoring
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
				if [glob.entry, glob.LANGUAGE, key] == item [0:3] ] [0]
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
	

		def add(key, value):
			return desk.entry.set(key, value)
		def pop(key):
			
			index = [ index for index, item in enumerate(glob.context) 
			if glob.entry == item [0] and key == item [-2] ]
			# ['Desktop Entry', 'en_US', 'Version', '1.0'], [], [], ['Desktop Entry', 'en_US', 'Type', 'Application'], []

			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				

			return glob
		def remove(key):
			return desk.entry.pop(key)
			
		def get(key):
			
			
			getext =  [ item for item in glob.context 
			if [glob.entry, glob.LANGUAGE, key] == item [0:3]] 
			# ['Desktop Entry', 'en_US', 'Icon', 'geany']
			
			base, lang, key, value = getext [0] if getext else [None]*4
			# [None]*4 -> defactoring
			# when not found key
			
			return value
			
	class action:
		
		def getindex(action):
			# Mon Feb 19 08:03:03 CST 2024
			
			try:
				return [ index for index, item in enumerate(glob.context) 
			if "%s %s" % (glob.action, action)  == item [0] ]
			except:
				return None
				# action: defactoring
				
		def group(key, value):
			return test.group(key, value, desk.action)
			
			# export.test.group(key, value, desk.action)
			# key, value, base=None, index=None, action=None
			
			
		def set(key, value, action):
			index = desk.action.getindex(action)
		
			return test.string(key, value, base=None, index=index, action=action)
			# export.test.string(key, value, base=None, index=index, action=action)
			
			"""
			
			[Desktop Entry]
			Exec=/usr/share/myapp/test
			Name=myapp
			Icon=face-heart

			
			"""
			
			# glob.context
		def add(key, value):
			return desk.action.set(key, value)

		def pop(key):
			

			index = [ index for index, item in enumerate(glob.context) 
			if "%s %s" % (glob.action, desk.action.base.key) == item[0] and key == item [-2] ]
			# ['Desktop Action test', None, None, None], [], [], []
			
			
			for index in index:
				# index: [3, 4, 5]
				
				del glob.context [index] [:]
				
				
			return glob
		def get(key):
			
			
			
			getext =  [ item for item in glob.context 
			if ["%s %s" % (glob.action, desk.action.base.key), glob.LANGUAGE, key] == item [0:3]] [0]
			# ['Desktop Action test', 'en_US', 'Icon', 'geany']
			base, lang, key, value = getext
			
			
			
			return value
class getitem:

		
	def __setitem__(self, key,value):
		desk.entry.set(key=key, value=value) 
class Base:
	Entry = getitem()
	
	entry = desk.entry
	action = desk.action
	
	
	def print_file():
		
		arr = []
		
		"""
		
		[Desktop Entry]
		Exec=/usr/share/myapp/test
		Name=myapp
		Icon=face-heart
		
		[Desktop Action X]
		Name=test
		
		
		"""
		
		for items in glob.context:
			
			if items:
				# defactoring
				
				base, lang,key, value = items
				
				if lang is None and key is None and value is None: 
					yield "[%s]" % (base)
					
				else:
					
					if lang == glob.LANGUAGE: 
						
							yield "%s=%s" % (key, value)
					else: yield "%s[%s]=%s" % (key, lang, value)
	
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



def content(name):
	
	
	glob.path = desktop.path(name) 
	
	# solution
	del glob.context [:]
	
	"""
	
	solutions:
	
	a) close open files.
	b) F2C
	c) del context
	d) one class
	
	
	
	application: system module
	content: testing
	
	
	Q: When the content module is used together with another module (application) 
	the same result a returning !
	
	
	sample: 
	
	for item in application():
		name = content(item).entry.get("Name")
		
		output: geany
				geany
				geany
				..
				..
				..
				

	solution:
	
	del glob.context [:]
	
	"""

	if not glob.path:
		
		glob.push(["Desktop Entry", None, None, None])
		glob.index.entry = 0
		
		# set yada group yok iken
		# calisma klasorunde kisayol olustur
		
		
	else:
		
		
		items = [  item.strip('[') .strip(']') 
		for item in open(glob.path).read().splitlines() 
		if item  ] 
		
		
		
		for index, item in enumerate(items):
			""" select: entry or action """

			if item.startswith('#'):
				continue
				

			if item.startswith(glob.entry) or item.startswith(glob.action):
				
				glob.select = item
				
				if item.startswith(glob.entry):
					glob.push([item, None, None, None])
					glob.index.entry = index
					
				elif item.startswith(glob.action):
					
					

					glob.push([item, None, None, None])
					glob.index.action = index
			else:
				
				items = item.split(chr(61))
				if "[" and "]" in  items [0]:
					
					
					key, lang, value = items [0] [0: items[0].index("[")], items [0] [items[0].index("[")+1: items[0].index("]")], items [1] 
					glob.push([ glob.select, lang, key, value ])
					
					
				else:
					glob.push([ glob.select, glob.LANGUAGE, items[0], items[1] ])
					
					
	return Base			
	




	

  
	
