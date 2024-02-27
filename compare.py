

from filecmp import cmp


tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
print(cmp(tuple1, tuple2))
print (cmp(tuple2, tuple1))
print (cmp(tuple2, tuple1))
