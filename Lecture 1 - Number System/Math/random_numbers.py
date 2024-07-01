import random

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print("Random float between 0.0 and 1.0:", random_float)
# Example Output: Random float between 0.0 and 1.0: 0.3745401188473625

# Generate a random integer between two values (inclusive)
random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)
# Example Output: Random integer between 1 and 10: 7

# Generate a random float between two values
random_uniform = random.uniform(1.0, 10.0)
print("Random float between 1.0 and 10.0:", random_uniform)
# Example Output: Random float between 1.0 and 10.0: 5.431945018642115

# Choose a random element from a list
random_choice = random.choice(['apple', 'banana', 'cherry'])
print("Random choice from list:", random_choice)
# Example Output: Random choice from list: banana

# Generate a random sample from a list without replacement
random_sample = random.sample(range(1, 11), 3)
print("Random sample of 3 elements from range 1 to 10:", random_sample)
# Example Output: Random sample of 3 elements from range 1 to 10: [4, 7, 2]

# Shuffle a list randomly
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("Shuffled list:", sample_list)
# Example Output: Shuffled list: [3, 5, 1, 4, 2]

# The `random.randrange(start, stop, step)` function generates a random integer within a range from `start` to `stop-1`, with increments defined by `step`.
random_randrange = random.randrange(1, 10, 2)
print("Random integer from range 1 to 10 with step 2:", random_randrange)
# Example Output: Random integer from range 1 to 10 with step 2: 3
# It generates a random integer from the sequence `[1, 3, 5, 7, 9]`. The `step` of `2` means it picks every second number starting from `1` up to `9` (excluding `10`).