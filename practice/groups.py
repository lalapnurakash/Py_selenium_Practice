import re

search_box='''ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrst
01234567890

Mr.akash
Mr.smith
mr.adams

!@#$%^&*({}|\/?>,<./...........
 ddddaaaa
+9165364328731
+9273578931
'''


# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# print(m.groupdict())

#{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

# if __name__ == '__main__':
#sep = re.search(r'((?!_)\w)\1+', input())
# print(sep.group(1) if sep else -1)
#


# pattern=re.compile(r'[+]91\d+')
# matches=pattern.finditer(search_box)
# for match in matches:
#     print(match)

# regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.



# import re
# P = input()
#
# print (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 1)

'''  float digit check    '''
# lst=[input() for _ in range(int(input()))]
# for i in lst:
#     if i=="0":
#         print("False")
#     else:
#         try:
#             float(i)
#         except:
#             print("False")
#         else:
#             print("True")

# import re
# m = re.search(r"([a-z0-9])\1{1,}", input())
#
# print(m.group()[0]) if m else print(-1)
#
# import re
# matches=re.findall(r'[aeiou]|[AEIOU]','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

'''***check vowels  ***'''

# pattern = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])'
#
# ar = re.findall(pattern, input())
#
# if len(ar) > 0:
#     for i in ar:
#         print (i)
# else:
#     print (-1)


''' aafgarefedsf
aaa
(-1, -1)'''

# import re
#
# string = input()
# subString = input()

# ptrn = re.compile(subString)
# m = ptrn.search(string)
# if m:
#     while m:
#         print(f"({m.start()}, {m.end() - 1})")
#         m = ptrn.search(string, m.start() + 1)
#
# else:
#     print("(-1, -1)")

''' verify mobile number '''

for _ in range(int(input())):
  regmob=re.compile(r'^[7-9][0-9]{9}$')
  print('Yes' if (regmob.match(input()) )else 'No')








