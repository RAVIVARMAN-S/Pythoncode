#example 
#input=2,3,-1,5
#input=2
#output=3

a=input().split(",")
b=int(input())

for i in range(len(a)):
    a[i]=a[int(i)] #storing as integer
  
c=sorted(a) #sorting as ascending order
kth_largevalue=c[-b] 
print(kth_largevalue)
    
