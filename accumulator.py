n = int(input("enter a positive integer till which you want the sum of the numbers to be calculated:"))
total = 0
for i in range(1,n+1):
	total += i
print("The sum of the numbers from 1 to", n, "is", total)


#using while loop
n = int(input("enter the number upto which you want to find the sum:"))
i = 0
sum = 0
while i<=n:
	sum += i
	i += 1
print("the sum of number from 0 to", n, "is:",sum)
