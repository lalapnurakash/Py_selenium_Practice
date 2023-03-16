import re
s='aheelin the modificahahions'
print(re.findall(r'[i|m]o','aheelin the modificahahions '))
#start with th
print(re.findall(r'\bth',s))
#end with th
print(re.findall(r'in\b',s))


