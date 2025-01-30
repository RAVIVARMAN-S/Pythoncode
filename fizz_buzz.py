def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz") #if i divisible by both 3 and 5
        elif i % 3 == 0:
            print("Fizz") #divisible only by 3
        elif i % 5 == 0:
            print("Buzz") #divisible only by 5
        else:
            print(i)


fizz_buzz(int(input("enter the number:")))
