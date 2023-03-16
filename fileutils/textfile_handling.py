try:
    f_demo = open("PythonSample.txt", "r+")
    f_demo. write("\nWelcome to Tutorial gateway")
    print(f_demo.seek(22))
   # f_demo = open("PythonSample.txt", "r")
    print( f_demo.readline())
    print(f_demo.tell())
    print('\nName = ', f_demo.name)
    print('Mode = ', f_demo.mode)
    print('closed? = ', f_demo.closed)
except OSError:
    f_demo.close()
    print("OSError")


