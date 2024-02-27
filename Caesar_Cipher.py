text = '12345'
key = 3
encrypted_text = ''

for char in text:
    if char.isalpha():  
        shifted = ord(char) + key
        if char.islower():
            if shifted > ord('z'):
                shifted -= 26  
        elif char.isupper():
            if shifted > ord('Z'):
                shifted -= 26  
        encrypted_text += chr(shifted)
    else:
        encrypted_text += char  

print(encrypted_text)
