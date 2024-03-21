#data types in python
number = 90 #number
decimal = 80.30 #float
com = 3+4j #complex
word = "This is a String Data Type" #string
isSanjay = True #boolean
ls = [1,2,3,4,5,6,7] #list
tup = (1,2,3,4,5,6,7) #tuple
person = {"name": "sanjay", "age":26} #dict
colors = {"red" , "blue", "yellow"} #sets

print(type(number))
print(type(decimal))
print(type(com))
print(type(word))
print(type(isSanjay))
print(type(ls))
print(type(tup))
print(type(person))
print(type(colors))


def name_setter():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(first_name + " " + last_name, end="???")
    print(first_name, last_name)


def form():
    name_setter()
    department_setter()


def department_setter():
    dep = input("Select your department: ")
    print(dep)


form()

