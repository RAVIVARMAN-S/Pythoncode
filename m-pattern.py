#inverted m pattern
n = int(input("enter the num:"))

for i in range(1, n + 1):
    stars = i
    spaces = 4 * (n - i)
    row = ("* ") * stars + (" ") * spaces + ("* ") * stars
    print(row)
