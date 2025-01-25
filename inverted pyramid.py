a=int(input())
for i in range(a):
    b=" "*i #spacing by index value
    c="*"*(2*(a-i)-1) 
    print(b+c)
