# def fibonacci_of(n):
#     if n in {0, 1}:  # Base case
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
#
#
# [fibonacci_of(n) for n in range(15)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# Function for nth Fibonacci number
#
# def Fibonacci(n):
# 	if n<= 0:
# 		print("Incorrect input")
# 	elif n == 1:
# 		return 0
# 	elif n == 2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)
#
# print(Fibonacci(10))


def fibonacci(n):
	if n <= 0:
		return "Incorrect Output"
	data = [0, 1]
	if n > 2:
         for i in range(2, n):
            data.append(data[i-1] + data[i-2])
            print(data[i-1] + data[i-2])
	return data[n-1]

print(fibonacci(9))

