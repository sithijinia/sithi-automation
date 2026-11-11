class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show(self):
        print("User:", self.username, "| Password:", self.password)

user1 = User("standard_user", "secret_sauce")
user2 = User("sithi", "abcd1234")

user1.show()
user2.show()