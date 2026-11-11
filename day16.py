try:
    age = int(input("How old is your daughter: "))
    print("Next year she will be" , age +1)

except ValueError:
    print("Please Enter a valid number.")