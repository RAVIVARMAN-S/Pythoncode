def compare(a,b):
    
    if(a>b):
        ms="Win"
    elif(a==b):
        ms="Draw"
    else:
        ms="Lose"
    return ms
    

a= int(input("enter the score:"))
b= int(input("enter the score:"))

compare_result = compare(a,b)

print(compare_result)
