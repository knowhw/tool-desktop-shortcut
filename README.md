
## #Installation
~~~bash
git clone https://github.com/knowhw/tool-desktop-shortcut.git
~~~


## Set [Languages Codes]( http://gist.github.com/knowhw/0adeb98e98f319efe0b668697042a737 )
```bash
export HELLO_WORLD='tr, bg, bh, bn, br, bs, ca mk, zh-CN, zh-TW'
```

## Solution
```py


from shortcuts import Key
from shortcuts import Content
import shortcuts



test = Content("bix")

test.Entry ["Name"] = "Yeap"
test.Entry ["Exec"] = "/usr/share/app/bix"
test.Entry ["Icon"] = "yeap"
test.Entry ["Categories"] = "InstantMessaging"
test.Entry ["Type"] = "Application"


# Entry Group
test.entry.group (key="Name", value="Yeap")


```



## Sample Output 
```

[Desktop Entry]
Name[tr]=Evet
Name[bg]=да
Name[bh]=हँ, हँ, हँ
Name[bn]=হ্যাঁ
Name[br]=None
Name[bs]=Da
Name[ca]=sí
Name[mk]=Да
Name[zh-CN]=是的
Name[zh-TW]=是的
Name=Yeap
Exec=/usr/share/app/bix
Icon=yeap
Categories=InstantMessaging
Type=Application


[Desktop Action X]
Name=Yeap


```

## What is that now!

This module enables users to effectively manage their shortcuts in Linux desktop environments, enhancing user experience and optimizing personal workflows. Users can get customized desktop solution management solutions by integrating them into their own module applications.






