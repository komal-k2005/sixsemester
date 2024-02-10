no=int(input("enter the number"))
rev=0
i=0
while no!=0:
    rev=no%10
    no=no//10
    print(rev,end="")