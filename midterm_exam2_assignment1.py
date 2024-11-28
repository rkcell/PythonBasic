'''
შექმენით პროგრამა, სადაც გვექნება Students კლასი.
მას უნდა ჰქონდეს ატრიბუტები: Name, Age, Student_ID და Grades.
კლასს უნდა ჰქონდეს ინფორმაციის გამოსატანი მეთოდი, სტუდენტების საშუალო ქულების
დასათვლელი მეთოდი და ყველაზე მაღალქულიანი სტუდენტის გამოვლენის მეთოდი.
სტუდენტების შესახებ ინფორმაციას წაიკითხავთ ფაილიდან, რომელსაც აქვე მივამაგრებ.
ეს ფაილი უნდა ჩამოტვირთოთ და პროგრამაში დაამატოთ ფაილის გახსნის ფუნქციაც
(*არ გადაიტანოთ ფაილიდან ინფორმაცია პირდაპირ) ფაილს ჰქვია Student_data . Students
კლასის ობიექტები უნდა შეიქმნას ამ ფაილის  მიხედვით.
'''


class Student:
    def __init__(self, name, age, student_id, grade):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = int(grade)

    def info(self):
        return f"Student Name: {self.name}, age: {self.age}, student_id: {self.student_id}, grades: {self.grade}"

    @classmethod
    def calculate_average_grade(cls, students_data):
        if not students_data:
            return 0
        total_grades = 0
        for student in students_data:
            print(student.info())
            total_grades+=student.grade
        return total_grades / len(students_data)

    @classmethod
    def find_highest_grade_student(cls, students_data):
        if not students_data:
            return 0
        highest_grade=0
        for student in students_data:
            if student.grade>highest_grade:
                highest_grade=student.grade
                highest_student=student
        return highest_student


def read_students_from_file(filename):
    students_data=[]
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, age, student_id, grades = line.strip().split(',')
                student = Student(name, age, student_id, grades)
                students_data.append(student)
            return students_data
    except:
        print(f"An error occurred!")

def main():
    filename = "Student_data.txt"
    students_data=read_students_from_file(filename)
    avg_grade=Student.calculate_average_grade(students_data)
    print(f"\nAverage Grade for students above is: {round(avg_grade, 2)}")
    highest=Student.find_highest_grade_student(students_data)
    print(f"\nHighest Student grade is: {highest.name} with grade {highest.grade}")

if __name__ == '__main__':
    main()



