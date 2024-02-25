



##  #Solution
```py
from au.desktop import content
desk = content("discord")

desk.Entry ["Exec"] = "/usr/share/discord/Discord"

desk.Entry ["Icon"] = "discord"
desk.Entry ["Type"] = "Application"
desk,Entry ["Terminal"] = "false"
desk.Entry ["Categories"] = "Network;InstantMessaging;"



test = desk.entry.group(key="Name", value="Discord")

for item in test.print_file():
	print(item)


```



## #Sample Output [/usr/share/applications/myapp.desktop]
```
[Desktop Entry]

Name=Discord
Exec=/usr/share/discord/Discord
Icon=discord
Type=Application
Categories=Network;InstantMessaging;
Path=/usr/bin

[Desktop Action X]
Name=test


```
