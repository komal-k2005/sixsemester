num=int(input("enter number"))
sum=0
rev=0
while num!=0:
    rev=num%10
    sum=rev+sum
    num=num//10
print(sum)    