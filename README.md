



```py
from au.desktop import content
```

##  #Solution 1 [set]
```py
desk = content("MyApp")


desk.Entry ["Exec"] = "/usr/share/myapp/test"
desk.Entry ["Name"] = "MyApp"

test = desk.action.set(key="Name", value="test", action="X")


```

##  #Solution 2 [set]
```py

desk.entry.set(key="Exec", value="/usr/share/myapp/test")
desk.entry.set(key="Name", value="MyApp")

test = desk.action.set(key="Name", value="test", action="X")

```


## #Group Key

```py

test = desk.entry.group(key="Name", value="MyApp")

```


```py
for item in test.print_file():
    print(item)
````

## Sample Output [/usr/share/applications/MyApp.desktop]
```
[Desktop Entry]
Exec=/usr/share/myapp/test
Name=myapp

[Desktop Action X]
Name=test
```
