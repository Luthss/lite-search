import sys
# Ask user for username
username = input("Enter username: ")

# Print the username
print(f'Hello {username}')

# Print the user arguments
print("Your arguments are:")


for count, item in enumerate(sys.argv):
    if count == 0:
        continue
    print(f'arg {count} is: {item}')

