with open('pi_few.txt','r') as file_pi:
    read_line1 = file_pi.readline()
    read_line2 = file_pi.readline()
    read_line3 = file_pi.readline()
    read_line1.strip 
    read_line2.strip 
    read_line3.strip  
    stict_string = read_line1 + read_line2 + read_line3 
    string_type = stict_string.replace("\n", '')
    print(string_type)
float_type = float(string_type)
print(float_type)    
new_float = float_type * 10
print(new_float)
