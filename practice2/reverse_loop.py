import getpass
import os


s=[2,53,65,4,5]
for i in range(len(s)-1,0,-1):
    print(s[i])
for k in range(len(s)-1,-1,-1):
    print(s[k],end=" ")
    pass

for m in reversed(s):
    print(m)
print(getpass.getuser())
print(os.environ)




