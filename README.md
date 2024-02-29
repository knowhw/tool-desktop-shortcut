



##  #Solution
```py


from au.shortcuts import content
import au.shortcuts


# solution

desk = content("bix")


# desk.entry.group(key="Name", value="geany")
desk.entry.set(key="Icon", value="face-heart")

# desk.Entry ["Terminal"] = "false"


# icon = desk.entry.get("Icon")

# name = desk.action.get("Name", action_key="X")

# desk.entry.set(key="Exec", value="/usr/share/myapp/test")
# desk.entry.set(key="Name", value="bix")

# desk.entry.pop(key="Categories")
# desk.action.popitem(key="Name")


desk.action.group(key="Name", value="bix", action_key="X")
# desk.entry.pop(key="Name")

# desk.action.group(key="Name", value="bix", action_key="X")
# desk.action.pop(key="Icon")





print(au.shortcuts.print_file())




```


## #Sample Output 
```
[Desktop Entry]

Name=Bix
Exec=/usr/share/app/bix
Icon=bix
Type=Application
Categories=Network;InstantMessaging;
Path=/usr/bin

[Desktop Action X]
Name=test


```

## What is that now!

Bu modül, Linux masaüstü ortamlarında kullanıcıların kısayolları etkin bir şekilde yönetmelerini sağlayarak kullanıcı deneyimini artırır ve masaüstü iş akışlarını optimize eder.
Kullanıcılar, modülü kendi uygulamalarına entegre ederek özelleştirilmiş masaüstü kısayol yönetimi çözümleri oluşturabilirler.

Modülün ana özellikleri şunlardır:
- Masaüstü kısayolları oluşturma, düzenleme, silme ve güncelleme.
- Mevcut kısayolları yönetme.
- Kısayolları kategorilere ayirma ve bu kategorileri yönetme.




