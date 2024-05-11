tmp = float(input("Input Temperature: "))
unit = str(input("Input Unit of temperature: "))
#making if-else statements or conditions for swiping the temperatures....
if unit == "Celsius":
    f = 9/5 * tmp + 32
    print(f, "Degree Fahrenheit")        

elif unit == "Fahrenheit" :
    C = 5/9 * (tmp - 32)
    print(C, "Degree Celsius")

#Also i can add infinite whie loop for better user experience....    

    


