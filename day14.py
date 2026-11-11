def greet(name):
    print("Hello",name)
    print("Welcome to Swag labs")

def is_valid_email(email):
    return "@" in email

greet("Sithi")
email=input("Enter email: ")

if is_valid_email(email):

   print("Email is accepted.")

else:

    print("Please enter a valid email.")