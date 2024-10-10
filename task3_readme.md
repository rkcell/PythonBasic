Homework: Grocery Shopping System

You are tasked with creating a simple Grocery Shopping System using functions, lists, tuples, and
loops.
The goal is to build a system where users can add items to a grocery list, remove items, view the
total cost
of their items, and find the most expensive item.

Task Description:

1. Grocery List Structure:
The grocery list should be a list of tuples where each tuple contains the item name and its price.
For example:
grocery_list = [('apple', 1.50), ('bread', 2.00), ('milk', 1.25)]

2. Functions to Implement:

- `add_item(grocery_list, item)`:
- A function to add an item to the grocery list. The item should be a tuple with the item name and
price.

- `remove_item(grocery_list, item_name)`:
- A function to remove an item from the list based on the item's name. If the item is not found,
print a message.

- `total_cost(grocery_list)`:

- A function to calculate the total cost of all items in the grocery list. Use a loop to sum the prices.

- `find_most_expensive(grocery_list)`:
- A function to find the most expensive item in the list and return it. Use a loop to compare item
prices.

3. User Interaction:
- Use a loop to continuously ask the user if they want to add, remove, view the total cost, or find
the most expensive item.
- Display the grocery list after each operation.

4. Validation:
- Ensure that the system handles invalid inputs, such as trying to remove an item that doesn't exist
or adding an item with an incorrect price.