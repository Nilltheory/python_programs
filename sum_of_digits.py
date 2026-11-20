n = int(input("Enter a positive integer: "))
original = n
total = 0

if n <= 0:
    print("invalid input")
else:
    while n != 0:
        digit = n % 10
        total += digit
        n = n // 10

    print("The sum of the digits of", original, "is", total)