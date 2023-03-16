import re

A=set(map(int, input().split()))
issuperset=True
for n in range(int(input())):
   B=set(map(int, input().split()))
   if (A.intersection(B)!=B or A==B):
        issuperset=False
        break
print(issuperset)

m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}





