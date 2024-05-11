while True:
 ui = input("User input: ")
 altered_string = ""
 if ui != 'q':
  for char in ui:
   if char.islower():
     altered_string += char.upper()
   elif char.isupper():
    altered_string += char.lower()
   else: 
    altered_string += char
    print("case altered: ", altered_string) 

  