'''
A file named grades.txt contains a list of students and their grades in the following format:
Alice,85
Bob,78
Charlie,92
Diana,88
Edward,76
Read the file and display each student's name and grade.
Calculate and print the class average grade.
Find and print the name of the student(s) with the highest grade.
Save the students who scored below the class average to a new file named below_average.txt.
Add functionality to allow the user to add a new student and their grade to the file. Ensure the file gets updated.
'''
students={}
below_average={}
f = open("grades.txt")
for line in f:
    result_line=line.strip().split(",")
    students[result_line[0]]=int(result_line[1])
f.close()

print(students, )

avg=sum(students.values())/len(students)
print(f"Average grade is: {avg}")
highest_grade=max(students.values())
for key,value in students.items():
    if value==highest_grade:
        print(f"Highest Grade Student found {key} with grade {value}")
    if value<avg:
        #print(f"Below average student found: {key} with grade {value}")
        below_average[key]=value

print(below_average)
f = open("below_average.txt", "w")
below_string=""
for k,v in below_average.items():
    below_string+=f"{k},{v}\n"

f.write(below_string)