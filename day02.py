print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$:"))
tip = int(input("What percentage tip would you like to give?\nPercent:"))
ppl = int(input("How many people to split the bill?\nPeople:"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / ppl
print(f"Each person should pay: ${bill_per_person:.2f}")