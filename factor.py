n = int(input("enter the number of which you want to find the factors of:"))
count = 0
if n <= 0:
  print("invalid input")
else:
  for i in range(1,n+1):
    if n%i == 0:
      count += 1
      print(i)
  print("The number of factors of", n, "is", count)

#this part of the code is to find prime numbers

  if count == 2:
    print("the given number" , n, "is a prime number")
  else:
    print("it is not a prime number")

