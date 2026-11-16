pencils = 49
n = pencils // 12

while n >= 0:
    remaining = pencils - n * 12

    if remaining % 5 == 0:
        print("12-pencil boxes:", n)
        print("5-pencil boxes:", remaining // 5)
        break

    n -= 1
else:
    print("No exact packing is possible.")