'''
1. დაწერეთ ფუნქცია სახელად "update_student", რომელიც პარამეტრებად მიიღებს მოცემულ students ლექსიკონს, "student_id"-ის და ლექსიკონს,
რომელიც შეიცავს ახალ ინფორმაციას - "new_info". ფუნქციამ უნდა განაახლოს სტუდენტის შესახებ ინფორმაცია.
 ფუნქციამ უნდა იმუშაოს მოცემული ტიპის ლექსიკონებზე.
2. new_info- თავისთავად იქნება {"name": "Nika" , "age": 23} ასეთი ტიპის ლექსიკონი, რომელიც studentIDის მიხედვით დაემატება თითოეულს.
from gi.overrides.GObject import new_name
'''

students = {
    "student1": {
        "name": "Nika",
        "age": 23
    },
    "student2": {
        "name": "Nino",
        "age": 21
    },
    "student3": {
        "name": "Salome",
        "age": 25
    }
}

new_info={}
# print(students)

def update_student(students, std_id, new_info):
#This function updates students dictionary by std_id
            return students[std_id].update(new_info)


while True:
    std_id = input("Please enter ID of the student for update: ")
    if std_id in students:
        new_info["name"] = input("Please enter new name: ")
        new_info["age"] = int(input("Please enter new age value:"))
        break
    print(f"Student with ID '{std_id}' not found, try again in format 'studentX' where X is integer...")


update_student(students, std_id, new_info)

#Pretty print the 'students' dictionary:
for x, obj in students.items():
    print(x)
    for y in obj:
        print("    "+ y + ':', obj[y])