a=int(input("enter the number:"))
if(a%4==0 and a%100!=0) or (a%400==0):
    print("leap year")
else:
    print("not a leap year")
