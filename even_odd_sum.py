n = int(input("enter an integer:"))
sum = 0
count = 0
for i in range(1,n+1):
	if i%2 == 0:
		sum += i
	else:
		count += i
print("The sum of even numbers from 1 to", n, "is", sum)
print("The sum of odd numbers from 1 to", n, "is", count)