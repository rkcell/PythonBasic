mydict={
    "apple":100,
    "pear":30,
    "carrot":24,
    "vegetable": 45
}

usr_key=input("Enter the key: ")
try:
    print(f"The value for {usr_key} is {mydict[usr_key]}")
except:
    print(f"Key '{usr_key}' not found in dictionary")