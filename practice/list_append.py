# N = int(input())
# commands = [input() for _ in range(N)]
# my_list = []
# for command in commands:
#    cmd , *args = command.split(' ')
#    if cmd == 'print':
#      print(my_list)
#    else:
#      task = f"my_list.{cmd}({','.join(args)})"
#      exec(task)

# if __name__ == '__main__':
#     N = int(input())
#     list_1=[]
#     for i in range(N):
#         s=input().split()
#         if s[0]=="insert":
#             list_1.insert(int(s[1]),int(s[2]))
#         elif s[0]=="reverse":
#             list_1.reverse()
#         elif s[0]=="remove":
#             list_1.remove(int(s[1]))
#         elif s[0]=="append":
#             list_1.append(int(s[1]))
#         elif s[0]=="sort":
#             list_1.sort()
#         elif s[0]=="pop":
#             list_1.pop()
#         elif s[0]=="print":
#             print(list_1)

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (600, 'ruby'))
print(scores)