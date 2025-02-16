def is_automorphic(num):
    square = num ** 2
    return str(square).endswith(str(num))

num = int(input("Enter a number: "))

if is_automorphic(num):
    print("Automorphic number")
else:
    print("Not an Automorphic number")
