import hashlib

def isValidPassword(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

def hashPassword(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

user_data = []

num_users = int(input("Enter the number of users: "))

for i in range(num_users):
    username = input(f"Enter username for user {i + 1}: ")
    

    while True:
        password = input(f"Enter password for user {i + 1}: ")
        if isValidPassword(password):
            break  
        else:
            print("Weak Password. Please enter a password that is at least 8 characters long and contains both letters and numbers.")

    hashed_password = hashPassword(password)
    user_data.append((username, hashed_password))
    

print("\nStored Passwords and Hashes:")
for username, hashed_password in user_data:
    print(f"{username}: {hashed_password}")
    print("Storing in Database.....")
