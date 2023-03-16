def decor1(func):
  def inner1():
      x = func()
      print("inner1 x :" ,x)
      print("inner1")
      return x * x

  print("decor1")
  return inner1

def decor(func):
    def inner():
       x = func()
       print("inner x :" , x)
       print("inner")
       return 2 * x #20

    print("decor")
    return inner

@decor1
@decor
def num():
   return 10

print(num())