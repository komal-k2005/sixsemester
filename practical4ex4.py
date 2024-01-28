s1=int(input("enter s1 marks"))
s2=int(input("enter s2 marks"))
s3=int(input("enter s3 marks"))
s4=int(input("enter s4 marks"))
s5=int(input("enter s5 marks"))
total=s1+s2+s3+s4+s5
avg=total/5
if avg>75:
    print("grde A")
elif avg>55 and  avg<75:
    print("grade B")
elif avg>=40 and avg<55:
    print("grade c")
else:
    print("fail")    
    