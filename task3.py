# Grocery Shopping System

# users can add items to a grocery list, remove items,
# view the total cost of their items, and find the most expensive item.

#NEEDS IMPROVEMENT: - items quantity currently not included to the system, so total cost can be improved

grocery_list = [('apple', 1.50), ('bread', 2.00), ('milk', 1.25)]

def adding_item(grocery_list):
# A function asks user the data to add an item to the grocery list. The item should be a tuple with the item name and price.
    while True:
        user_item = input("Please enter the name of the item and the price separated by \",\" (column) ")
        if "," in user_item:
            new_item=user_item.split(', ')
            new_item[1]=float(new_item[1])
            if len(new_item) ==2 and new_item[1] >= 0:
                print(add_item(grocery_list,tuple(new_item)))
                break
        else:
            print("Your input is not validated, please re-enter valid data")

def add_item(grocery_list, item):
    #check the item to be tuple with size of 2
    if isinstance(item, tuple) and len(item)==2:
        grocery_list.append(item)
        result = "item is successfully added to the grocery list"
    else:
        result = "type error, item not added"
    return result



def remove_item(grocery_list):
    #A function to remove an item from the list based on the item's name. If the item is not found, print a message.
        user_item = input("Please enter the name of the item for removal: ")
        for i in grocery_list: #searching grocery_list and finding match
            if i[0]==user_item:
                grocery_list.remove(i)
                result = "item is successfully removed"
                break
            else:
                result= "item not found, try another name"

        return result



def total_cost(grocery_list):
    # A function to calculate the total cost of all items in the grocery list. Use a loop to sum the prices.
    items_sum=0
    for i in grocery_list:
        items_sum+=i[1]
    return f"Total cost of all items is {items_sum}"

def find_most_expensive(grocery_list):
    #A function to find the most expensive item in the list and return it. Use a loop to compare item prices.
    highest_price=0
    most_expensive=''
    for i in grocery_list:
        if i[1]>highest_price:
            highest_price=i[1]
            most_expensive=i[0]
    return f"Most expensive item is {most_expensive}, it priced {highest_price}"

while True:
    user_input = input("Please enter the command- add (A), remove (R), view (V) the total cost, find (F) most expensive product or X to exit: ").lower()

    match user_input:
        case "r":
            print("perform remove operation…")
            print(remove_item(grocery_list))
        case "a":
            adding_item(grocery_list)
        case "v":
            print("perform view operation …")
            print(total_cost(grocery_list))
        case "f":
            print("perform find operation …")
            print(find_most_expensive(grocery_list))
        case "x":
            print("Exiting...")
            break
        case _:
            print("wrong variant if operation !!!")