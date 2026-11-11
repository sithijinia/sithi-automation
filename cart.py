product = input("Product Name: ")
price = float(input("price: "))
quantity = int (input("quantity: "))

if quantity < 1:
  print("Quantity must be at least 1.")

else:

  total = price * quantity

  print("product:",product)
  print("Total price:",total)