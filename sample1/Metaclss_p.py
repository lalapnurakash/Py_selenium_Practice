import gc
from collections import Counter
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



class Meta(type):

    def __new__(self,class_name, bases, attrs):
        a={}
        for item,val in attrs.items():
            if item.startswith("__"):
                a[item]=val
            else :
                a[item.upper]=val
        return type(class_name,bases,a)





c=Counter(['B','B','A','B','C','A','B','B','A','C'])
c.update(['D'])
print(c)
class dog(metaclass=Meta):
    x=5
    y=19
    def hello(self):
       print("hi")


dog1=dog()

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a > b else b

print(min)


# Python3 program for demonstrating
# closing a coroutine

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")
corou.__next__()
corou.send("Dear Atul")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
sleep(4)
# get element
print(driver.get_screenshot_as_png())
# get rect
driver.close()
gc.collect()
