
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print(" It's nice")
print("Done")

#Ternary operator
age = 20
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# me: str = "ke"
# print(me)

#logical operator [ and, or, not ]
high_income = True
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

print(not True)