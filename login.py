users = {"sithi": "abcd1234", "standard_user": "secret_sauce"}

username = input("Username: ").strip().lower()
password = input("Password: ").strip()

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Wrong username or password.")