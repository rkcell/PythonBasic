thisdict = {"apple": 2,
            "strawberry":5}

print(thisdict)
print(thisdict["apple"])

for key, value in thisdict.items():
    print(key, value)

thisdict2 = thisdict.copy()
thisdict2 = dict(thisdict)

x = ("key1", "key2", "key3")
y=0
thisdict3= dict.fromkeys(x,y)
print(thisdict3)

print(thisdict.get("apple"))