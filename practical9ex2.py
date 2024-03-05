dictionary={'google':1,'facebook':2,'microsoft':3}
dictionary2={'gfc':1,'youtube':3,'microsoft':2}
dictionary.update(dictionary2)
for  key,values in dictionary.items():
    print(key,values)