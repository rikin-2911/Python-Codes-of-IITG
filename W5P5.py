while True:
    vowels = "aeiouAEIOU"
    inp = str(input("Enter your message: "))
    for char in inp:
        if char not in vowels:
            print(char, end = "")
    print() 
