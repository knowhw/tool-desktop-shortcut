
from desktop import glob

class test:		
	
	def print_file():
		
		arr = []
		
		"""
		
		[Desktop Entry]
		Name=myApp
		GenericName=Internet Messenger
		Exec=/usr/share/test
		Icon=test
		Type=Application
		Categories=Network;InstantMessaging;
		Path=/usr/bin
		[Desktop Action X]
		Name=test
		
		"""
		
		
		for (base, lang,key, 
	value ) in glob.context:
			
			if lang is None and key is None and value is None: 
				yield "[%s]" % (base)
				
			else:
				
				if lang == glob.LANGUAGE: 
					
						yield "%s=%s" % (key, value)
				else: yield "%s[%s]=%s" % (key, lang, value)
				
	def group(key, value, base):
		

		"""
		
		[Desktop Entry]
		Name[xh]=uvavanyo
		Name[yi]=פּרובירן
		Name[yo]=idanwo
		Name[zu]=test
		Name=test
		GenericName=Internet Messenger
		Exec=/usr/share/test
		Icon=test
		Type=Application
		Categories=Network;InstantMessaging;
		Path=/usr/bin
		
		
		"""
		
		googleapis = "/translate_a/single?client=gtx&dt=t&"
		query = "http://translate.googleapis.com%ssl=auto&tl=%s&q=%s"
		
		
		
		for lang in [ item.get(glob._) for item in glob.lang.findall('name') if item.get(glob._) ]:
		
		
			base, lang, key = [ getattr(glob, "entry"), lang, key ]
			exists = [  item for item in glob.context if item [0:3] == [ base, lang, key ] ]
		
		
			if not exists:
				
				
				query = query % (googleapis, lang, value)
				response = glob.loads(glob.urllib.request.urlopen(query).read()) [-9][-1][0]
				# base, lang, key, value
				
				index = [  index for index, item in enumerate(glob.context) 
				if  item [0] == base and item [1] == glob.LANGUAGE and item [2] == key ]
				
				
				
				glob.insert( index [0], [ base, lang, key, response ])
				# print(base, lang, key, response)

		return test
		
		
	def string(key=None, value=None, base=None, index=None, action=None):
		# export.test.string(key, value, base=None, index=index, action=action)
		
		
		
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
				glob.context.insert(glob.index.entry + 1, [glob.entry, glob.LANGUAGE, key, value] )
				""" key yoksa """
			else:
				

				glob.context[index][-1] = value
				""" key varsa """
				
		return test
	
	def file_update(self):
		from desk import temp
		
		
		tempfile, name = temp.filetouch(content)
		tempfile.pkexec.mv2(glob.path)
		
		return glob
		
