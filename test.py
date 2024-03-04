
from shortcuts import Key
from shortcuts import Content
import shortcuts



test = Content("bix")
# io.elementary.wingpanel

#test.Entry ["Name"] = "Yeap"
#test.Entry ["Icon"] = "yeap"
# test.Entry ["Comment"] = "Get help with GNOME"
#test.Entry ["OnlyShowIn"] = "GNOME;Unity;"
#test.Entry ["StartupNotify"] = "true"
#test.Entry ["Terminal"] = "false"
#test.Entry ["Type"] = "Application"
#test.Entry ["Categories"] = "GNOME;GTK"
#test.Entry ["Actions"] = "X;"


# test.action.set (key="Name", value="Yeap", action_key="X")
test.entry.set (key="Name", value="deneme")
# test.action.group (key="Icon", value="Yeap", action_key="X")

# test.action.group (key="Name", value="Yeap", action_key="Y")
# test.entry.group (key="Comment", value="Yeap")
# First IN Last OUT


test = shortcuts.print_content()
print(test)
"""
TODO: FILO - LIFO
test.LIFO

"""


#2.3.0
#3.5.2.2

#4.3.5


# TODO: gozden gecirme ve kod iyilestirmesi....
#1: TRANSLATE ortak func.
#2: Entry Actions -> append action_key
#3: LANG: value to text
#4: bash: export set LANGUAGE
#5: fonks. ve siniflari say



item = Key.getitem("Name")
print(item.text)



  
