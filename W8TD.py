""" A FILE MANAGING AND MANIPULATING APPLICATION BUILD WITH THE HELP OF OOPS CONCEPT AND FILE HANDLING CONCEPTS!!"""

from collections import Counter  #To count the number of occurences of anything(Here words)
import re # regex (Useful in some cases !)

class FileReader:
    #Takes a file path as input and returns the contents of the file as a string.
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r', encoding ='utf-8') as file:
            contents = file.read()
            return str(contents)


class TextAnalyzer(FileReader): 
    # Initializes the class with the text content from the file.  
    def __init__(self, text):
        self.text = text
        self.words = self._tokenize_words()

    #Returns the total number of words in the text.
    def get_word_count(self):
        words = self.text.split()  #Split method is used to split the words by whitespaces.
        return len(words) 
    
    
    def _tokenize_words(self):
        """Helper method to tokenize words in the text."""
        words = [
            word.strip('.,!?') for word in self.text.split() 
            if word.strip('., !?') and not word.isspace()
        ]

        return words 

    # Returns the total number of sentences in the text.
    def get_sentence_count(self):
        count = 0
        for char in self.text:     #This is my method, for complex sentences we need for improvent in this!
            if char == ".":
                count = count + 1
            if char == "?":         #Split method can also be used(slightly more efficient than this!)
                count = count + 1
            if char == "!":
                count = count + 1    
        return count         

    # Returns the average length of words in the text.
    def get_average_word_length(self):
        word_lengths = []
        words = self.text.split()
        word_count = len(words)         #Total words
        word_lengths = sum(len(word) for word in words) #length of all words
        avg_word_count = word_lengths / word_count if word_count != 0 else 0
        return avg_word_count

    #Returns a list of the n most frequently occurring words in the text, along with their frequencies.
    def get_top_words(self, n):     #This function is critical (Understand it properly !)
        word_count = Counter(self.words) # Frequencies of words
        print(f"Word counts: {word_count}")
        return  word_count.most_common(n)
        


class ReportGenerator(TextAnalyzer):
    # Initializes the class with an instance of the TextAnalyzer class.
    def __init__(self, analyzer):
        self.analyzer = analyzer 

    #Generates a summary report containing the following information
    def generate_report(self, top_n = 20):
        word_count = self.analyzer.get_word_count()
        sentence_count = self.analyzer.get_sentence_count()
        average_word_lenth = self.analyzer.get_average_word_length()
        top_words = self.analyzer.get_top_words(top_n)

        #Designing the report
        report = f"---------------TEXT ANALYSIS REPORT---------------\n"
        report += f"Word Count: {word_count}\n"
        report += f"Sentence Count: {sentence_count}\n" 
        report += f"Average Word Length: {average_word_lenth:.2f}\n" 
        report += f"Top {top_n} Words: \n" 

        for word, frequency in top_words:
            report += f" {word}: {frequency}\n"

        return report

    # Saves the generated report to a specified file path.
    def save_report(self, file_path, top_n = 20):
        #self.filepath = file_path
        report = self.generate_report(top_n)
        with open(file_path, 'w') as file:
            file.write(report)    


"""                             Main Function                            """
file_path = str(input("Enter the NAME of the text file or PATH of the text file with '.txt' extension: \n"))

print("-" * 15)

obj1 = FileReader(file_path)
print(f"The contents of the file are: \n {obj1.read_file()}")

print("-" * 15)

obj2 = TextAnalyzer(obj1.read_file())

print(f"The total number of words in this file are: \n {obj2.get_word_count()}")

print("-" * 15)

print(f"The total number sentences in this file are: \n {obj2.get_sentence_count()}")

print("-" * 15)

print(f"The average word length in this file is: \n {obj2.get_average_word_length()}")

print("-" * 15)

print(f"The top occuring words with their frequencies in tis file are: \n {obj2.get_top_words(20)}")

print("-" * 15)

print("The text analysis of this file is as below: \n")
obj3 = ReportGenerator(obj2)
print(obj3.generate_report())

print("-" * 15)

new_file_path = str(input("Please enter the path where the report should be save. (With suitable extension. Preferred '.txt'.\n"))

obj3.save_report(new_file_path)

print("-" * 15)
print("Your report is successfully saved to " + new_file_path + " file.")
print("-" * 15)
print("TASK ENDED SUCCESSFULLY..!")