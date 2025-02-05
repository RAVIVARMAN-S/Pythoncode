#q1.The pattern has two parts – both mirror reflections of each other. 
#The base of the triangle has to be at the bottom of the imaginary mirror and the tip at the top.


a=int(input("ente the number:"))
for i in range(1,a+1): #upper part of the mirror triangle
    s=(" ")*(a-i)
    print(s+i*" *")
for i in range(1,a+1): #lower part of the mirror triangle
    s=(" ")*(i-1)
    print(s+((a-i+1)*" *"))

#output
ente the number:6
     

      *
     * * 
    * * *
   * * * *
  * * * * *
 * * * * * *
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *

#q2.simple interest 
#Simple Interest = (P x T x R)/100 
#Input :  P = 10000
#R = 5
#T = 5
Output : 2500


      
p=int(input("enter the amount:"))
t=int(input("enter the time duration:"))
r=int(input("enter the rate of interest:"))

SI=(p*t*r)/100   #simple interest formula
print(int(SI))   #change from float to integer


