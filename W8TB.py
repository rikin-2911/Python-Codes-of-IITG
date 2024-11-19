class FileManager:
    #Initializes the class with a file path !
    def __init__(self, file_path):
        self.file_path = file_path

    #Reads the contents of the file and returns them as a string.
    def read_contents(self):
        with open(self.file_path, 'r') as file:
            contents = file.read()
            return str(contents)   

    #Overwrites the contents of the file with the provided new_contents string.
    def write_contents(self, new_contents):
        with open(self.file_path, 'w') as file:
            contents = file.write(new_contents)
            return str(contents)
    
    #Appends the new_contents string to the existing contents of the file.
    def append_contents(self, new_contents):
        with open(self.file_path, 'a') as file:
            contents = file.writelines(new_contents)
            return str(contents) 
        

            
#example for function "read_contents"
ex_1 = FileManager('Example_for_week8.txt')
otp_readContents = ex_1.read_contents()
print(otp_readContents)

#example for function "write_contents"
stringcontent = "My name is Rikin."

otp_writeContents = ex_1.write_contents(stringcontent)
print(otp_writeContents)

#example for function "append_contents"
newContent = ["Hi, My name is Rikin.\n", "How are you ?\n", "I hope you are fine.\n"
              "Thank you !\n"]
otp_appendcontents = ex_1.append_contents(newContent)
print(otp_appendcontents)
