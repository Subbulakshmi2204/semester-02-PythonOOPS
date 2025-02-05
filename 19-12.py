import re
word="SImple regular expression example"
result=re.findall("gula",word)
print(result)

import re
word="SImple regular expression example regular"
result=re.findall("gula",word)
print(result)

import re
space=re.search("\s",word)
print("\n The first space is at:",space.start())
