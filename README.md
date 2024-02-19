
<div align="left">

</div>

<br/>



## Installation
~~~bash
git clone https://github.com/knowhw/tool-desk-shortcut.git
~~~

## Sample Work File [/usr/share/applications]
~~~
[Desktop Entry]
Type=Application
Version=1.0
Name=Geany
Exec=geany %F
Icon=geany
Terminal=false
Categories=GTK;Development;IDE;
StartupNotify=true
Keywords=Text;Editor;

~~~

## #Tool usage

~~~python
from desk import application
import desk


base = application("myapp")


# desk.set(base.entry, "Name", "MyApp")
desk.group(base.entry, "Name", "MyApp")

# desk.add_action("new", "Name", "test-new-tab")
# desk.pop_action("new")

keywords = desk.get(base.entry, "Name")
# print (keywords)


desk.print_file()
~~~




