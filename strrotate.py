a=input("enter the string:")
b=int(input("enter the number:"))
length=len(a)
rotate=a[b:]
print(rotate+""+a[:b])
