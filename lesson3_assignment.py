direction = int(input("Enter the Robot direction code (11,12,13,14): "))-11
turn= int(input("Enter the Robot turn code (-1,0,1): "))

dirnames=["North", "West", "South", "East"]
turn_names=["Right", "Straight", "Left"]

if direction+turn >3:
    finaldirection = direction+turn-4
elif direction+turn <0:
    finaldirection = direction+turn+4
else:
    finaldirection=direction+turn

print(f"You entered the direction {dirnames[direction]}")
print(f"You entered the turn {turn_names[turn+1]}")
print(f"Robots final direction is: {dirnames[finaldirection]}")


