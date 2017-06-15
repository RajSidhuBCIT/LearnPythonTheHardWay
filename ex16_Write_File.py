from sys import argv

script, filename = argv

print(f"We're gpnna erase {filename}")
print("if you dont want that hit CTRL-C (^C).")
print("if you do want that her ENTER")

input("?")

print("Opening file....")
target = open(filename, 'w')

print("truncating file. Bye!")
target.truncate()

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Now i'm gonna write to the file")

newline = "\n"
target.write(line1 + newline + line2 + newline + line3 + newline)

#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("Finally, we close the file")
target.close()
