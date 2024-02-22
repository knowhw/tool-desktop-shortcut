

from desktop import glob
from desktop import export
from listdir import application


class desktop:

	def path(name):
		
		listdir = application()
		# usr/share/applications
		
		return listdir.get(name)
		
class getitem(dict):
	def __getitem__(self, key):
		return super().__getitem__(key) if key in self else None
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
			
			
			
			return export.test.group(key, value, desk.entry)
			# key, value, base=None, index=None, action=None


		def set(key=None, value=None):
			
			index = desk.entry.getindex(key)
			return export.test.string(key=key, value=value, index=index)
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
			return export.test.group(key, value, desk.action)
			# key, value, base=None, index=None, action=None
			
			
		def set(key, value, action):
			index = desk.action.getindex(action)
		
			return export.test.string(key, value, base=None, index=index, action=action)
			
			"""
			
			[Desktop Entry]
			Name=test
			Icon=face-heart
			[Desktop Action test]
			Name=test
			Icon=test
			[Desktop Action X]
			Name=test
			Exec=/usr/bin/test
			
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
class Base:
	Entry = getitem()
	
	entry = desk.entry
	action = desk.action
	
	
	def set():
		
		for key, value in Base.Entry.items():
			desk.entry.set(key=key, value=value)
	
		return export.test
		
def create():
	""" calisma klasorunde kisayol olustur """


def content(name):
	
	
	glob.path = desktop.path(name) 
	
	
	if not glob.path:
		
		glob.push(["Desktop Entry", None, None, None])
		glob.index.entry = 0
		
		# set yada group yok iken
		# calisma klasorunde kisayol olustur
		
		
	else:
		
		items = [ item.strip('[') .strip(']') 
		for item in open(glob.path).read().splitlines() 
		if item  ] 
		
		
		
		for index, item in  enumerate(items):
			
			
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
	"""
	
	[Desktop Entry]
	Icon[zu]=test
	Icon[yo]=test
	Icon[yi]=test
	Icon[xh]=test
	Icon=test
	Name[yo]=test
	Name[zu]=test
	Name[yi]=test
	Name[xh]=test
	Name=test
	Exec=/usr/share/test/test
	Type=Application
	Categories=Network;InstantMessaging;
	Path=/usr/bin
	[Desktop Action X]
	name=test

	"""




	

  
	
