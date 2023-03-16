import math

if __name__ == '__main__':
    num = int(input().strip())
    match num:

       case num if (math.fmod(num,2))!=0 or ((num%2)==0 and 6<=num<=20):
            print("Weird")
            "break"
       case num if (((num%2)==0) and 2<=num<=5) or ((num%2)==0 and num>20) :
            print("Not Weird")
            "break"



