
class person:

 def __init__(self,name,AGE):
    self.__name=name
    self.__age=AGE
 @property
 def Name(self):
     return self.__name
 @Name.setter
 def setName(self,value):
     self.__name=value
p=person("akash",23)
p.setName="f"
print(p.Name)

def func(mypa:int) ->int:
     return f"{mypa+10}"
def otherfun(par:str):
    print(par)
otherfun(func(10))