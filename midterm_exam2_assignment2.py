'''
წაიკითხეთ ექსელის ფაილში არსებული ინფორმაცია,
სადაც მოცემულია: მსახიობის ანაზღაურება  სხვადასხვა ფილმებისა და წლების მიხედვით.
აქვე არის სხვა დამატებითი ინფორმაციაც, თუმცა თქვენ უნდა  ააგოთ გრაფიკი,
რომელიც იქნება James Bond-ის ხელფასის ცვლილება წლების მიხედვით.
x ღერძზე ააგეთ წლები, ხოლო y ღერძე ხელფასი
გამოიყენეთ Pandas ბილიოთეკა ფაილის გასახსნელად (ფაილის ფორმატია: .csv)
გამოიყენეთ matplotlib  გრაფიკის ასაგებად.
* შენიშვნა, plot(), მეთოდს x და y პარამეტრებად შეგიძლიათ გადასცეთ პირდაპირ
Year და Salary სვეტები, რომელსაც გამოიძახებთ ასე data["Year"], data["Salary"]
'''

import pandas as pd
import matplotlib.pyplot as plt

try:
    data= pd.read_csv("jamesbond.csv")

    salary_data=data[" Salary"]
    year_data=data["Year"]

except FileNotFoundError:
    print("File doesn't exist")

plt.title("James Bond actor salary change")
plt.plot(year_data, salary_data)
plt.xlabel("Year", fontdict={"fontsize":15})
plt.ylabel("Salary in million USD", fontdict={"fontsize":15})
plt.show()
