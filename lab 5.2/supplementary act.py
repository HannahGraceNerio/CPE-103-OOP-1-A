with open("NERIO.txt", "w") as file:
    file.write("This file shows how to create and read a text file.\n")
    file.write("The file contains a basic analysis of file operations in Python.\n")
    file.write("Each line here will be read and printed one by one.\n")

with open("NERIO.txt", "r") as file:
    for line in file:
        print(line.strip())