from sys import argv

script, fileName = argv

txt = open(fileName)
print(f"Here is your file: {fileName}")
print(txt.read())

print("Type the file name again:")
file2 = input("> ")
txt2 = open(file2)
print(txt2.read())
