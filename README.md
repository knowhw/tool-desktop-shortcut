
## #Installation
~~~bash
git clone https://github.com/knowhw/tool-desktop-shortcut.git
~~~


## #Set Languages Codes
```bash
export HELLO_WORLD='tr, bg, bh, bn, br, bs, ca mk, zh-CN, zh-TW'
```


##  #Solution
```py


from shortcuts import Key
from shortcuts import Content
import shortcuts



test = Content("bix")

test.Entry ["Name"] = "Yeap"
test.Entry ["Exec"] = "/usr/share/app/bix"
test.Entry ["Icon"] = "yeap"
test.Entry ["Type"] = "Application"

test.Entry ["Path"] = "/usr/bin"
test.Entry ["Categories"] = "InstantMessaging"

test.action.group (key="Name", value="Yeap", action_key="X")

```



## #Sample Output 
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
Type=Application
Path=/usr/bin
Categories=InstantMessaging
[Desktop Action X]
Name=Yeap



```

## What is that now!

Bu modül, Linux masaüstü ortamlarında kullanıcıların kısayolları etkin bir şekilde yönetmelerini sağlayarak kullanıcı deneyimini artırır ve masaüstü iş akışlarını optimize eder.
Kullanıcılar, modülü kendi uygulamalarına entegre ederek özelleştirilmiş masaüstü kısayol yönetimi çözümleri oluşturabilirler.

Modülün ana özellikleri şunlardır:
- Masaüstü kısayolları oluşturma, düzenleme, silme ve güncelleme.
- Mevcut kısayolları yönetme.
- Kısayolları kategorilere ayirma ve bu kategorileri yönetme.




