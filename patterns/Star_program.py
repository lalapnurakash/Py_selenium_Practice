star=5
space=0
for i in range(4):
    for j in range(space):
        print(" ",end="")
    for k in range(star):
            print("*",end="")
    star-=2
    space+=1
    print("",sep="")