import getpass

name = input("Enter name: ")
enc = getpass.getpass("Pass is: ")  # Hides input for better security

# Name and enc conditions
if not name.isalpha():
    print("Error! only letters allowed in name.")

elif not enc.isdigit():
    print("Password should only have numbers!")

# Password length condition
elif len(enc) < 8:
    print("Password should be at least 8 digits long!")

# If both are valid, output
else:
    print("Name is:", name, "Password is:", enc)
