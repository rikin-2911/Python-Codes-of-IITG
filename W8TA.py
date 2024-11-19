#Creating a function for reading a file and returning contents of that file.
def file_reader(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        return str(contents) 
    
#Example.!
opt = file_reader('GTU SEM 3 EXAM TT.txt')
print(opt)