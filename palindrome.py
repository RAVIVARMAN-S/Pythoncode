a=str(input("enter the string:"))
for i in range(len(a)):
    if(a[i]==a[len(a)-i-1]):
        print("it's a palindrome")
    else:
        print("it's not a palindrome")
