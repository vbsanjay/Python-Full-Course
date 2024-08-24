import os

os.chdir('/Users/vbsanjay/My Code/Python/Python – Full Course/Lecture 14 - File I:O')
print("Current working directory:", os.getcwd())

filename = "example.txt"
mode = 'a'

try:
    with open(filename, mode) as file:
        # perform file operation here
        content = file.append(" Sanjay")
        print(type(content))
except FileNotFoundError as e:
    print("File not found:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
