attendance = float(input("Enter your attendance percentage: "))
assignments = int(input("Enter the number of assignments submitted: "))

if attendance < 0 or attendance > 100 or assignments < 0:
    print("invalid input")
elif attendance >= 75 and assignments >= 8:
    print("eligible")
else:
    print("not eligible")