# Map

# using for loop
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = []
for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print(uppered_pets) # output: ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']

# using map
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets) # output: ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result) # output: [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]

# zipping 2 list
roll_number = [1,2,3,4,5,6]
name = ["sanjay", "vijay", "dhinakaran", "vishaal", "mohamed"]
print(list(zip(roll_number, name)))

# zipping using map function
print(list (map( lambda x, y: (x, y), roll_number, name) ) )