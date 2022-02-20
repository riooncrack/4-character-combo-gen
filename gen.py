import string
import random

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits

num = 0
desc = ""

while num <= 10000:
    combined = lowercase + numbers
    password = "".join(random.sample(combined,4))
    desc += f"{password}\n"
    num += 1

file = open("4charactercombos.txt", "w")
file.write(desc)
file.close()
print("Success!")