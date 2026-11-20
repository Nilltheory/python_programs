def outer():
  def inner():
    print("hello")
  return inner

clo = outer()
print(clo)