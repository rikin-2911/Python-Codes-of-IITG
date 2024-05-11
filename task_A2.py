while True:
    mass = input("Mass: ")
    c = 300000000
    if mass != 'q':
        mass = int(mass)
        E = mass*c*c    
        print(E, "Joules" )  
    else: 
       break  
print("Exit")    