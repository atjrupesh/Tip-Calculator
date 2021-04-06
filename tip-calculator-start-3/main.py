print("Welcome to Tip calculator! ")
bill = int(input("What was the total bill? "))
tip = int(input("How much Tip would you like to give? "))
split = int(input("How many persons should split the bill? "))

percent = tip/100
print(percent)

n_value = round(bill*percent,2)
# n_value = (bill*percent)
print(n_value)

final = n_value + bill
print(final)

_1split = final/split
print(f"You need to pay {_1split} per head")

