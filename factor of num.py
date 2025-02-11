#factors of given number by def function
def factors_of_n(number):
    for i in range(1,number+1):
        if(number%i==0): #gives factors of n if it divisible by iterate range 
            print(i,end=" ") 
            
            
    

number = int(input())
factors_of_n(number) # call the  function
