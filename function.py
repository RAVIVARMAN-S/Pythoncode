def get_discount(amount):
    if(500>amount):
        print("5%")
    elif(500<=amount<=2500):
        print("10%")
    else:
        print("20%")# Complete this function


amount = int(input())
get_discount(amount)# Call the get_discount function
