# Create a dict
mydict = {
    1:1,
    "2":2,
}
print(type(mydict))
print("Created a dict")
print(mydict)

# Insert an element in the dict
mydict["red"] = "apple"
print("Insert an element in the dict")
print(mydict)

# Update an element in the list
mydict["2"] = "Two"
print("Update an element in the dict")
print(mydict)

# Access an element in the dict
print("Access an element in the dict")
print(mydict[1])
print(mydict["red"])
print(mydict.get("2"))

# Iterating over a dict
print("Iterating over a dict")
for key in mydict:
    print(key, mydict[key])
for value in mydict.values():
    print(value)
for item in mydict.items():
    print(item)
for key, value in mydict.items():
    print(key, value)

# Delete an element in the dict
print("Delete an element form the dict")
del mydict["red"]

# Advanced dict
# Dict within a dict
mydict = {
    "names":{
        1: "Arjun",
        2: "Sanjay",
        3: "Vijay"
    }
    ,
    "age":{
        "Arjun": 20,
        "Sanjay": 21,
        "Vijay": 22
    }
}
print(mydict)
print(mydict["names"])
print(mydict["names"][1])
print(mydict["age"]["Arjun"])

# List within a dict
mydict = {
    "names":["Arjun", "Sanjay", "Vijay"],
    "age":[20, 21, 22]
}
print(mydict)
print(mydict["names"][0])
print(mydict["age"][0])

# Creating a dict with 2 list
names =["Arjun", "Arjun", "Sanjay", "Vijay"]
age = [20, 21, 22, 28]
mydict = dict(zip(names, age)) # duplicates are taken care by python itself
print(mydict) # output: {'Arjun': 21, 'Sanjay': 22, 'Vijay': 28} 

# Keys View (dict_keys)
my_dict = {"a": 1, "b": 2, "c": 3}
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

# Values View (dict_values)
values_view = my_dict.values()
print(values_view)  # Output: dict_values([1, 2, 3])

# Items View (dict_items)
items_view = my_dict.items()
print(items_view)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
