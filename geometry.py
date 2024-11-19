PI = 3.14

def calculate_area_rectangle(length, width):
    # calculates and returns the area of a rectangle
    area_r = length * width  
    return area_r

def calculate_area_circle(radius):
    #calculates and returns the area of a circle
    area_c = PI * (radius ** 2)
    return area_c

def calculate_perimeter_rectangle(length, width):
    #calculates and returns the perimeter of a rectangle
    peri_r = 2 * (length + width)
    return peri_r

def calculate_circumference_circle(radius):
    # calculates and returns the circumference of a circle
    circum_c = 2 * PI * radius 
    return circum_c 
