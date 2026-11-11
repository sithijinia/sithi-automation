

for i in range(1, 6):

    print("Test case", i)

tries = 1
while tries <= 3:
    print("Login attempt", tries)
    tries = tries + 1
users = {"sithi": "abcd1234", "standard_user": "secret_sauce"}

print(users["sithi"])
print("sithi" in users)
print("rahim" in users)