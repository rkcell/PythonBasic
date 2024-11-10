'''
შექმენით კლასი, სახელად Project.
კლასს კონსტრუქტორებად უნდა ჰქონდეს title, project_duration, budget.
კლასს უნდა ჰქონდეს ფუნქცია full_info, რომელიც დააბრუნებს პროექტის შესახებ სრულ ინფორმაციას.
შექმენით Project კლასის 6 ობიექტი.
'''

class Project:
    def __init__(self, title, project_duration, budget):
        self.title=title
        self.project_duration=project_duration
        self.budget=budget

    def full_info(self):
        return f"Title: {self.title}, Duration: {self.project_duration} months, Budget: {self.budget} USD"

    def __str__(self):
        return self.full_info()

if __name__ == '__main__':
    project1=Project("Main Project", 6, 30000)
    print(project1)
    project2 = Project("Second Project", 5, 20000)
    print(project2)
    project3 = Project("Third Project", 3, 3000)
    print(project3)
    project4 = Project("Forth Project", 4, 40000)
    print(project4)
    project5 = Project("Fifth Project", 5, 5000)
    print(project5)
    project6 = Project("Sixth Project", 6, 6000)
    print(project6)
