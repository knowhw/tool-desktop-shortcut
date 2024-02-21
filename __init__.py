# https://youtu.be/_SfB348JGIA?list=RDGMEMJQXQAmqrnmK1SEjY_rKBGA&t=24


from desktop import glob
from desktop import export
# from desktop import translate

class desktop:

	def path(name):
		
		import os
		
		
		# global path_desktop_items
		path_desktop_items = [ os.path.realpath(item) 
		for item in os.listdir(glob.appdir) ]

		dictionary = {}
		""" dictionary: app list => usr share applications """
		
		
		for item in path_desktop_items:
			
			name2, extension = os.path.splitext(os.path.basename(item))
			
			dictionary [name2] = '%s/%s%s' % (glob.appdir, name2, extension)
			""" 'path':'%s/%s%s' % (glob.appdir, Exec, extension) """
		
		return dictionary.get(name)
		
class getitem(dict):
	def __getitem__(self, kelime):
		return super().__getitem__(kelime) if kelime in self else None
class desk:
	
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
			if glob.entry == item[0] and key == item [-2] ]
			# ['Desktop Entry', 'en_US', 'Version', '1.0'], [], [], ['Desktop Entry', 'en_US', 'Type', 'Application'], []
			
			
			for index in index:
				# index: [2, 3, 5]
				
				del glob.context [index] [:]
				
			return glob
		def remove(key):
			return desk.entry.pop(key)
			
		def get(key):
			getext =  [ item for item in glob.context 
			if [glob.entry, glob.LANGUAGE, key] == item [0:3]] [0]
			# ['Desktop Entry', 'en_US', 'Icon', 'geany']
			base, lang, key, value = getext
			
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
			Icon=geany
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
	# calisma klasorunde kisayol olustur
	content="[Desktop Entry]"
	
	
	return content
def content(name):
	
	
	glob.path = desktop.path(name) 
	
	
	if not glob.path:
		
		glob.push(["Desktop Entry", None, None, None])
		glob.index.entry = 0
		# calisma klasorunde kisayol olustur
		
	else:
		
		items = [ item.strip('[') .strip(']') 
		for item in open(glob.path).read().splitlines() if item  ] 
		
		
		
		for index, item in  enumerate(items):
			
			if item.startswith('#'):
				continue
				
			"""
			Desktop Entry
			Type=Application
			Version=1.0
			Name=Geany
			Exec=geany %F
			Icon=geany
			Terminal=false
			Categories=GTK;Development;IDE;
			StartupNotify=true
			Keywords=Text;Editor;
			Desktop Action test
			Name=Geany
			
			
			"""
			if item.startswith(glob.entry) or item.startswith(glob.action):
				""" select: entry or action """
				
				
				glob.select = item
				
				if item.startswith(glob.entry):
					
					
					glob.push([item, None, None, None])
					glob.index.entry = index
					


				elif item.startswith(glob.action):
					
					glob.push([item, None, None, None])
					glob.index.action = index
					
					
					
			else:
				
				key, value = item.split(chr(61))
				

				if key.find("[") > -1 and not key.find("]") > -1:
					
					glob.push([ glob.select, key [ key.find("[") + 1: key.find("]") ], key [ 0: key.find("[") ], value ])
					
					
					
				else:
					glob.push([ glob.select, glob.LANGUAGE, key, value ])
					

	return Base
	
	



	

  
	
