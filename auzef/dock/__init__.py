
from auzef import temp

from auzef.dock import glob
from auzef.listdir import application


class launcher:
	
	
	content = """
[PlankDockItemPreferences]
Launcher=file:///usr/share/applications/%s.desktop
"""
	
	def remove_from_dock(self,item):
		
		glob.os.system("rm %s/%s.dockitem > /dev/null 2>&1" % (glob.dockdir, item))
		
		
	def add_dock(self, item):
		
		apps = application()
		
		if item in apps:
		
			content = launcher.content % item
			
		
			path = '%s/%s.dockitem' % (glob.dockdir, item)
			# /home/linux/.config/plank/dock1/launchers/spyder3.dockitem
			
			tempfile, name = temp.filetouch(content)
			tempfile.mv2(path)
			return path
		else:
			return 
		
	def pop(self, item):
		return launchers.remove_from_dock(item)
	
		
		



