

# fruits1 = ['apple', 'orange', 'kiwi']
# fruits2 = ['banana', 'cherry', 'berry']
# result = map(lambda a, b: a + b, fruits1, fruits2)
# print(list(result))
def square_func(num):
    return num ** 2


def tripple_func(num):
    return num * num * num


def four_func(num):
    return num ** 4


function_list = [square_func, tripple_func, four_func]

for i in range(1, 10):
    number = map(lambda x: x(i), function_list)
    print("For ", i, " = ", list(number))
fruits = ['apple', 'berry', 'kiwi']
print(fruits[1])
result = map(list, fruits)
print(list(result))
print(fruits)


class MainClass:

    def func_message(self):
        print('Welcome to Main')

class Child(MainClass):
    def func_child(self):
        print('This class is inherited from Main')

class ChildDerived(Child):

    def func_Derived(self):
        print('This class is inherited from Child')

print(issubclass(ChildDerived, Child))
print(issubclass(ChildDerived, MainClass))

print('------------')
print(issubclass(Child, MainClass))

print('------------')
print(issubclass(Child, ChildDerived))