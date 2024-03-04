a={1,2,3,4}
b={3,4,5,6}
c=a|b
d=a-b
e=a^b
f=a&b
print("union",str(c))
print("intersection",str(f))
print("difference",str(d))
print("symmetric difference",str(e))
del a
del b