# N, M = map(int, input().split())
# result = []
# for i in range(1, N + 1):
#     if i == int(N / 2) + 1:
#         result.append('WELCOME')
#     elif i < int(N / 2) + 1:
#         result.append('.|.' * (i * 2 - 1))
#     else:
#         result.append('.|.' * ((N + 1 - i) * 2 - 1))
# print('\n'.join(list(map(lambda x: x.center(M, '-'), result))))
# s="mwna"
# print(s.center(2,"-"))

number=10
space = len(bin(number)[2:])
for i in range(1, number + 1):
    f=str(i).rjust(space) + " "
    print(str(i).rjust(space) + " " + oct(i)[2:].rjust(space) + " " + (hex(i)[2:].upper()).rjust(space) + " " + bin(i)[
                                                                                                                2:].rjust( space))
print(space)

def print_formatted(number):
    for i in range(1, number + 1):
        width = number.bit_length()
        print(f'{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}')
    return None