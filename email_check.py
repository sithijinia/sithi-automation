email = input("Enter your email: ")
email = email.strip().lower()

if "@" in email:
    print("Valid email:", email)
else:
    print("Invalid email. Email must contain @")