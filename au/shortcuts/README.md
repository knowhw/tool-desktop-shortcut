

## Installation
~~~bash
git clone https://github.com/knowhw/tool-desktop-shortcut.git
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

~~~


```python



from au.shortcuts import content
import au.shortcuts


# solution


desk = content("geany")

# desk.entry.group(key="Name", value="geany")
# desk.entry.set(key="Icon", value="face-heart")
# desk.entry.set(key="Exec", value="geany %F")

desk.Entry ["Terminal"] = "false"
#desk.entry.pop("Name")

#icon = desk.entry.get("Icon")
#print("get: %s" % icon )


# desk.entry.set(key="Exec", value="/usr/share/myapp/test")
# desk.entry.set(key="Name", value="bix")

desk.entry.pop(key="Categories")
# desk.entry.set(key="Name", value="bix")
#if not actions:
# desk.entry.pop(key="Name")

desk.action.group(key="Name", value="bix", action_key="X")
#desk.entry.pop(key="Name")

#desk.action.group(key="Name", value="bix", action_key="X")
# desk.action.pop(key="Icon")

#name = desk.action.get("Name", action_key="X")
#print(name)
	
desk.action.popitem(key="Name")

print(au.shortcuts.print_file())
#for item in au.desktop.print_file():
#print(item)

```



