a=str(input("enter the string:"))
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        result=a[i:j]
        print(result)
