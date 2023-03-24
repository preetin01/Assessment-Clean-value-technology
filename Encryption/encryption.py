def encrypt(str):
    reversed_str=reversed(str)
    vowels={'a':'3','e':'8','i':'1','o':'9','u':'4'}
    replaced_string = ''
    for char in reversed_str:
        if char in vowels:
            replaced_string += vowels[char]
        else:
            replaced_string += char 
               
    encrypted_str = replaced_string + "abxu"    
    return encrypted_str 
     
# Driver Code        
str=input('Enter the string: ')
str=str.lower()
encrypted_str=encrypt(str)
print(encrypted_str)
