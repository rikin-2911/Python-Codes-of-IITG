def add(a, b):
    # This function will adding the two numbers and return their result 
    result = a + b
    return result 

def subtract(a, b):
    # This function will subtracting the two numbers and return their result
    result = a - b
    return result  

def multiply(a, b):
    # This function will multiply the two numbers and return their result
    result = a * b
    return result

def divide(a, b): 
    # This function will divide the first number by second and return their result
    if b == 0:
        print("The number " + str(a) + " cannot be divided by 0")
    else:
        result = a / b 
        return result          
