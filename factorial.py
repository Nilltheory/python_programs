n = int(input("enter an integer:"))
fact = 1

if n < 0:
	print("invalid input")
else:
	for i in range(1,n+1):
		fact *= i
	print("factorial of the number", n , "is", fact)