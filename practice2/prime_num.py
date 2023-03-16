# def prime(x, y):
#     prime_list = []
#     for i in range(x, y):
#        if i == 0 or i == 1:
#           continue
#        else:
#             for j in range(2,int(i/2)+1):
#                 print(int(i/2) +1)
#                 if i%j==0 :
#                     break
#                 else :
#                     prime_list.append(i)
#     return prime_list
#
# # Driver program
# starting_range = 2
# ending_range = 7
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
# 	print("There are no prime numbers in this range")
# else:
# 	print("The prime numbers in this range are: ", lst)
#
def sieve(x, y):
    numbers = [i for i in range(x, y + 1)]

    i = 0


    while i < len(numbers):
        if numbers[i] is not None:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                numbers[j] = None
        i += 1

    return [n for n in numbers if n is not None]


# Driver program
starting_range = 2
ending_range = 7
lst = sieve(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)

