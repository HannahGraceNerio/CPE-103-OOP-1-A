import os

# CREATE
with open("NERIO.txt", "w") as file:
    file.write("This is the first version of the file.\n")

# READ
print("Reading file:")
with open("NERIO.txt", "r") as file:
    print(file.read())

# UPDATE (APPEND MODE)
with open("NERIO.txt", "a") as file:
    file.write("This line is added to update the file.\n")

# READ AGAIN TO SHOW UPDATE
print("\nAfter updating the file:")
with open("NERIO.txt", "r") as file:
    print(file.read())

# DELETE
if os.path.exists("NERIO.txt"):
    os.remove("NERIO.txt")
    print("\nFile Nerio.txt has been deleted.")
else:
    print("File does not exist")