def string(str):
    k=0
    j=0
    for i in str:
      if(i.islower()):
            j=j+1
      elif(i.isupper()):
            k=k+1
    print("The number of lowercase characters is:")
    print(j)
    print("The number of uppercase characters is:")
    print(k)
string('KoMaL')
    