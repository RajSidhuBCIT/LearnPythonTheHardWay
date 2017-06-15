from sys import argv

script, userName = argv
prompt = '> '

print(f"Hi {userName} I am the script: {script}")
print("I have a few questions.")
print(f"Do you like me {userName}?")
likes = input(prompt)

print(f"Where do you live {userName}?")
lives = input(prompt)

print("What kind of computer do you have?")
comp = input(prompt)

print(f"""
Ok so you said {likes} about liking me.\n
You live in {lives}.\n
You have {comp} computer. Noice.
""")