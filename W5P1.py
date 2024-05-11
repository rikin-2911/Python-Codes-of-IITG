#Making a Factorial calculator
n = int(input("Enter the number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")    
if (n == 0) or (n == 1):
    if n == 0:
        print("Factorial of 0 is: 1")
    else:
        print("Factorial of 1 is: 1")    
else:    
   product = 1    
   for i in range(1 , n + 1 ):
       product *=  i
print("Factorial of", n ,"is", product)       
