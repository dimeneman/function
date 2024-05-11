# When we know we are going to get error on something we use the try and except method.
try:
    print ("Now computing hte result..")
    result = 5/0
    print("Computation is succesful")
except ZeroDivisionError:
    print("Failed to compute the result because you're trying to devide it with zero")
    result = None

print(result)
