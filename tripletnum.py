#triplet of num
num=int(input("enter the num:"))
for i in range(1,num):
    for j in range(i+1,num):
        for k in range(j+1,num):
            if(i+j+k==num):
                b=(i,j,k)
                print(b)
