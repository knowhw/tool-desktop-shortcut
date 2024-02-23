
from au import temp

from au.dock import glob
from au.listdir import applications


class launcher:
	
	
	content = """
[PlankDockItemPreferences]
Launcher=file:///usr/share/applications/%s.desktop
"""
	
	def remove_from_dock(self,item):
		
		glob.os.system("rm %s/%s.dockitem > /dev/null 2>&1" % (glob.dockdir, item))
		
		
	def add_dock(self, item):
		
		apps = applications()
		
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
	
		
		



