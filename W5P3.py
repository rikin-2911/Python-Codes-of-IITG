num = 47
gnum = int(input("Enter the number between 0 to 100: "))
abdiff = abs(gnum - num)
while True:
    if abdiff == 0:
        print("Congruatulaions your guess is absolutely right and accurate..!") 
        print("-" * 35)
        break
    elif abdiff <= 5:
        print("You are very close to the right guess..!")
        print("-" * 35)
        break
    elif abdiff <= 10:
        print("You are still not close  to the right guess..!")
        print("-" * 35)
        break
    elif abdiff > 10:
        print("You are not even close to the right guess, Sorry, Try again !")    
        print("-" * 35)
        break
#print("Number of attempts for reaching the right guess are : "jfd)    

# Code is incomplete will do it afterwards!!!