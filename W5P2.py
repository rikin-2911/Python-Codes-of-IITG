while True:
    num = int(input("Enter any number: "))
    if num <= 0:
        print("Enter a valid positive integer..")
    elif num < 4:
        if num == 1:
            print(num, "is NOT Prime Number!")
        if num == 2:
            print(num, "is Prime Number!")
        if num == 3:
            print(num, "is Prime Number!") 
    elif num > 4:
        for i in range(2, num + 1):
           if num % i == 0:
               print("It is Not a Prime Number.")
             
# code is not valid or is in buliding stage
            