a=int(input("enter the number:"))
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(a):
    s=("  ")*(a-i-1)
    for j in range(i+1):
        s=s+b[j]+" "
    print(s)
