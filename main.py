# Sample database of usernames and passwords
user_database = {
    "admin": "project",
    "user1": "12345",
    "guest": "guest1"
}

def login():
    print("Welcome to the Login System!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and password matches
    if username in user_database and user_database[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password. Please try again.")

# Run the login function
login()
