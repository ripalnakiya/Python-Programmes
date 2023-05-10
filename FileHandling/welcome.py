import sys

name = input("Enter your name: ")

# For existing users
with open("customers.txt", "r") as file:
    for user in file:
        print(user)
        if (user[0:-1] == name):
          print(f"Hello {user}, Welcome back!")
          sys.exit()

# For new users
print(f"Hello {name}")

# file = open("customers.txt", 'a')
# file.write(name)
# file.close()

# This format is better than previous one coz we don't have to close the file explicitly
with open("customers.txt","a") as file:
    # file.write(name + '\n') We haven't used format string here
    file.write(f"{name} \n")
