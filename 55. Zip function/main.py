# aggregate elements from 2 or more iterables
# creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ["password", "abc123", "guest"]
login_dates = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords)

print(type(users))

for user in users:
    print(user)

users_list = list(zip(usernames, passwords))
print(users_list)
print(type(users_list))

user_data = zip(usernames, passwords, login_dates)
for user in user_data:
    print(user)
