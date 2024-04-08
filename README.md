
## Overview

This module enables users to effectively manage their shortcuts in Linux desktop environments, enhancing user experience and optimizing personal workflows. Users can get customized desktop solution management solutions by integrating them into their own module applications. [language codes]( http://gist.github.com/knowhw/0adeb98e98f319efe0b668697042a737 )


## Installation
~~~bash
git clone https://github.com/knowhw/tool-desktop-shortcut.git
~~~


## Set Language Code
```bash
export HELLO_WORLD='bg, bh, bn, bs, ca, mk, tr, zh-CN, zh-TW'
```

## Solution
```py


from desktop_file import Key
from desktop_file import Content
import desktop_file


test = Content("bix")

test.Entry ["Name"] = "Yeap"
test.Entry ["Exec"] = "/usr/share/app/bix"
test.Entry ["Icon"] = "yeap"
test.Entry ["Categories"] = "InstantMessaging"
test.Entry ["Type"] = "Application"


# Entry Group
test.entry.group (key="Name", value="Yeap")

# Item pop
# test.entry.popitem("Name")


# Item get value

# item = Key.getitem("Name")
# print(item.text)


test = desktop_file.print_content()
print(test)
```

<!-- This is commented out. 
## More Information
- [Documentation](https://pillow.readthedocs.io/)
- https://pillow.readthedocs.io/en/latest/handbook/concepts.html#size
-->








