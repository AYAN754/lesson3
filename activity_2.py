total_amount = int(input("enter the real amount: "))
sell_amount = int(input("enter sale amount: "))
if (sell_amount>total_amount):
    amount = sell_amount - total_amount
    print(f"you have a profit of {amount} Rs")
else:
    loss = total_amount - sell_amount
    print(f"you have a loss of {loss} Rs")