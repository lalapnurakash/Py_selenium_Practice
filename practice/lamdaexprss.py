# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'our')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)
import os

string="abcdcd"
sub_string="cd"
num = 0
for x in range(len(string) - len(sub_string) + 1):
    if sub_string in string[x:len(sub_string) + x]:
            num += 1
print(num)
print(dir(os))