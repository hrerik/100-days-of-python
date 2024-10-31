print("TIP CALCULATOR")

initial_bill = float(input("What was the total bill?\n$"))
tip = float(input("How much tip do you want to give (in percentage)?\n"))
num_people = int(input("How many people are you spliting the bill with?\n"))

bill_for_each = (initial_bill * (tip/100 + 1)) / num_people

print(f"Each one will pay ${round(bill_for_each,2)}.")
