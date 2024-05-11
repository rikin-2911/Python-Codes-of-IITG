print("Input your Details here: ")
print("--------------------------------")
str(input("Enter Student Name: "))
int(input("Enter Roll no: "))
min = float(input("Enter marks in Maths: "))
mip = float(input("Enter marks in Physics: "))
mic = float(input("Enter marks in Chemistry: "))
print("--------------------------------")
# Calculation of Grades for Subject Maths...
if min >= 90:
    Grade1 = "A"
elif 80 <= min < 90 :
    Grade1 = "B"
elif 70 <= min < 80:
    Grade1 = "C" 
elif 60 <= min <70:
    Grade1 = "D"
elif min < 60:
    Grade1 = "E"
#Calculation of Grades for Subject Physics...
if mip >= 90:
    Grade2 = "A"
elif 80 <= mip < 90 :
    Grade2 = "B"
elif 70 <= mip < 80:
    Grade2 = "C" 
elif 60 <= mip <70:
    Grade2 = "D"
elif mip < 60:
    Grade2 = "E"
#calculation of Grades for subject Chemistry...
if mic >= 90:
    Grade3= "A"
elif 80 <= mic < 90 :
    Grade3 = "B"
elif 70 <= mic < 80:
    Grade3 = "C" 
elif 60 <= mic <70:
    Grade3 = "D"
elif mic < 60:
    Grade3 = "E"    
#Output of Grades in Maths, Chemistry , and Pysics....
print("Here is the Grade Card:")
print("--------------------------------")
print("Grade in Maths: ", Grade1)
print("Grade in Physics: ", Grade2)
print("Grade in Chemistry: ", Grade3)
#Calculation of Overall Grades.......
og = (min + mip + mic) // 3
if og >= 90:
    og = "A"
elif 80 <= og < 90 :
    og = "B"
elif 70 <= og < 80:
    og = "C" 
elif 60 <= og <70:
    og = "D"
elif og < 60:
    og = "E"

print("Overall Grades: ", og)
print("--------------------------------")
print("Thank you!")

