import numpy as np
import time
pi_string = "" # Variable creation

#Defining a function for assinging 1M pi to the variable created
def load_pi_digits(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents
    
#defining another function for computimg percentage of each of (0-9) digits
def get_pi_one_gram_stats(num):
    total = 1000000
    calc = pi_string.count(num)
    percentage = ((calc / total) * 100)
    percentage = str(percentage) + " % "
    return percentage

#defining another function for checking if birthdate of user is there in 1M numbers in pie
def is_birthdate_in_pie(ddmmyyyy):
    start_time = time.time()
    date = pi_string.count(ddmmyyyy)
    end_time = time.time()
    final_time = start_time - end_time
    if date == 0:
        return print("Date not found in pie")
    else:
        return print("Date Found! and\nNum Occurrences: ", date,
                      "\nProcessing Time: ", final_time, " ms" "\nPress Ctrl + c for exiting loop")
        


#Example for Checking result of function 1:-   
pi_string = load_pi_digits('pi_1M.txt')
print(pi_string)
pi_string = pi_string.replace("\n", "")

#Example for checking result of function 2:-       
enter_num= str(input("Please enter any number for calculation of percentage of that number: "))  
percentage = get_pi_one_gram_stats(enter_num)
print(percentage)   

#Example for checking result of function 3:-    
while True: 
    user_date = str(input("Please input your Birthdate in the format of 'DDMMYYYY': ")) 
    user_date = is_birthdate_in_pie(user_date)
    print(user_date)
