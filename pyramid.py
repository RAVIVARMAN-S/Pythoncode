a=int(input())
num=1
for i in range(1,a+1):
    b=""
    for j in range(1,i+1):
        b=b+str(num)+" " 
      num=num+1 
    print(b)
