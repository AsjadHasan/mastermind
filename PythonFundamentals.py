"Q1. Self Introduction Card"

name = "Asjad"
age = 28
city = "Toyoake"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

"Q2. Suica Card Balance Check"

balance = 320
fare = 410
if balance < fare:
    print("Insufficient balance")
else:
    print("You can board the train")

"Q3. Train Fare Category"

age = 25
if age < 12:
    print("Child")
elif age <= 22:
    print("Student")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

"Q4. Shinkansen Countdown"

for i in range(10, 0, -1):
    print(i)
print("Departing Tokyo Station!")

"Q5. ATM Withdrawal Attempts"

correct_pin = 1234
guesses = [1111, 2222, 1234]
attempts = 0
access = False
while attempts < 3:
    pin = guesses[attempts]
    attempts += 1
    if pin == correct_pin:
        access = True
        break
if access:
    print("Access granted")
else:
    print("Card blocked")

"Q6. Konbini Shopping List"

items = ["onigiri", "tea", "bento"]
items.append("pudding")
items.remove("tea")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

"Q7. Name Formatter"

full_name = " tanaka yuki "
formatted_name = full_name.strip().title()
print(formatted_name)

"Q8. Vending Machine Dictionary"

vending = {
    "cola": 150,
    "water": 120,
    "coffee": 130
}
item = "coffee"
if item in vending:
    print(f"{item}: {vending[item]} yen")
else:
    print("Item not available")

"Q9. Consumption Tax Function"

def calculate_total(price):
    total = price * 1.10
    return round(total, 2)
print(calculate_total(100))
print(calculate_total(500))
print(calculate_total(1200))

"Q10. Osaka Weekly Temperature"

temps = [28, 31, 27, 33, 30, 29, 32]
highest = max(temps)
lowest = min(temps)
average = sum(temps) / len(temps)
print(f"Highest temperature: {highest}°C")
print(f"Lowest temperature: {lowest}°C")
print(f"Average temperature: {average:.2f}°C")