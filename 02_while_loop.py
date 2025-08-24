# Example 2 algorithm (while) —  3 Login attempts
# Correct password
correct_password = "admin123"


# Number of attempts
attempts = 0


# Allow up to 3 attempts
while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
        attempts += 1

if attempts == 3:
    print("Access denied")
