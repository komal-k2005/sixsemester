fn=0
sn=1
tn=sn+fn
print(fn)
print(sn)
for i in range (1,5):
    fn=sn
    sn=tn
    tn=fn+sn
    print(tn)