
Bu modül, kullanıcıların kendi kısayollarını oluşturmasına, düzenlemesine ve yönetmesine olanak tanır, 
masaüstü deneyimini kişiselleştirmelerini sağlar.
</br>


##  #Solution
```py
from au.desktop import content
desk = content("bix")


desk.Entry ["Terminal"] = "false"
desk.Entry ["Exec"] = "/usr/share/app/bix"
desk.Entry ["Icon"] = "bix"
desk.Entry ["Type"] = "Application"



```

```py
test = desk.entry.group(key="Name", value="bix")

for item in test.print_file():
	print(item)
```



## #Sample Output [/usr/share/applications/myapp.desktop]
```
[Desktop Entry]

Name=Discord
Exec=/usr/share/app/bix
Icon=bix
Type=Application
Categories=Network;InstantMessaging;
Path=/usr/bin

[Desktop Action X]
Name=test


```
