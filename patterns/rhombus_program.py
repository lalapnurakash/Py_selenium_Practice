star=0
space=4
for i in range(7):
    for j in range(space):
        print(" ",end="")
    for k in range(star):
            print("*",end="")
    if i <= 3:
        space -= 1
        star += 2
    else:
        star-=2
        space+=1


    print("",sep="")