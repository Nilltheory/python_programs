n = int(input("Enter the number of pages you want to print: "))

if n <= 0:
    print("invalid input")
else:
    if n > 50:
        total_cost = 50 * 3 + (n - 50) * 2
    else:
        total_cost = n * 3

    print("The total cost of the printout is", total_cost)