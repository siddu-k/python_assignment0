#gradechecker
score = int(input("eNter your score :"))

if score >=90:
    print("A")
elif score >= 80:
    print("B")    
elif score >= 70:
    print("C")   
elif score >= 60:
    print("D") 
else:
    print("F")     


#student grades
student_grades = {

    'siddu':'A',
    'ravi':'B',
    'Lahari':'A'
}

student_grades['raju']='F'

print(student_grades)

#writefile

file_be = open("example.txt", "w") 

file_be.write("content written to file")

file_say = open("example.txt", "r")

print(file_say.read())
