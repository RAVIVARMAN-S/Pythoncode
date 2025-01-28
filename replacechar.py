a=input()
c=""
for i in a:
    b=chr(ord(i)+1) #find ord of each char
    c=c+b #store the each char 
 
print(c.replace("!"," ")) #replace the empty space
 


