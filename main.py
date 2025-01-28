name = input("Enter name: ")
enc = input("Pass is: ")

#name and enc conditions
if not name.isalpha():
    print("Error! only letters allowed in name.")

elif not enc.isdigit():
    print("Password should only have numbers!")

#password length condition
elif len(enc) < 8:
    print("Password should be at least 8 digits long!")

# If both are valid,output
else:
    print("Name is:", name, "Password is:", enc)
