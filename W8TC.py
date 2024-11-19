import csv
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
        
class CSVDataManager(FileManager):
    #Initializes the class with a file path and an optional delimiter (default is a comma).
    def __init__(self, file_path, delimiter = ','):
        self.file_path = file_path
        self.delimiter = ','

    #Reads the contents of the CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    def read_data(self):
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print('{', row, '}')
    
    # Takes a list of dictionaries data and writes it to the CSV file, overwriting the existing contents.
    def write_data(self, data):
        with open(self.file_path, 'w', newline = "") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)   
    
    #Takes a list of dictionaries data and appends it to the existing contents of the CSV file.
    def append_data(self, data):
        with open(self.file_path, 'a') as csv_file:   
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
            
#Example-1 for testing on file 1
exp1 = CSVDataManager('csv_week8_ex.csv')            
print(exp1.read_data())

data = ['2911', 'Rikin Pithadia', '2', '97']
print(exp1.write_data(data))

data = ['3534', 'Rikin Pithadia', '2', '97']
print(exp1.append_data(data))

#Example-2 for testing on file 2
exp2 = CSVDataManager('csv_week8_ex2.csv')
print(exp2.read_data())

data2 = ['3744', 'ML-282', '4', 'Spring', '2024']
print(exp2.append_data(data2))