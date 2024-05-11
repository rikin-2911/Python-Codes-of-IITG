while True:
    inp = str(input("Enter the variable name in Camel case: "))
    for char in inp:
         if char.isupper():
           low = char.lower()
           rep = inp.replace(char, "_" + low)
           print(rep)
#still we can do more things like if someone enters name with more than one upper letter
# We do something more in this code !