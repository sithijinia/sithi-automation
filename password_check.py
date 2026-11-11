password = input("Enter Password: ").strip()

if len(password) == 0:
    print("Password can not be empty.")

elif len(password) < 8:
    print("Password must be at least 8 characters.")

else :
    print("Password accepted.")       