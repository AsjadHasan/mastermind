"""
T3. IC transit card (ICOCA style)
Problem statement
Model a prepaid IC card that a commuter taps at station gates. The card must never go below zero.
1. Create a TransitCard class whose constructor takes owner and a starting balance (yen).
2. Method charge(amount) adds money and prints the new balance.
3.Method tap(fare) deducts the fare and prints the new balance. If the balance is lower than the fare, print Insufficient balance. Please charge your card. and do not deduct anything.
4.Run the sequence of calls below in order.
"""  
class TransitCard:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def charge(self, amount):
        self.balance += amount
        print(f"New balance: ¥{self.balance}")
    def tap(self, fare):
        if self.balance >= fare:
            self.balance -= fare
            print(f"New balance: ¥{self.balance}")
        else:
            print("Insufficient balance. Please charge your card.")
owner = input("Enter card owner's name: ")
balance = int(input("Enter starting balance (yen): "))
card = TransitCard(owner, balance)
while True:
    print("\n1. Charge card")
    print("2. Tap at station gate")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = int(input("Enter charge amount (yen): "))
        if amount > 0:
            card.charge(amount)
        else:
            print("Charge amount must be positive.")
    elif choice == "2":
        fare = int(input("Enter fare (yen): "))
        if fare > 0:
            card.tap(fare)
        else:
            print("Fare must be positive.")
    elif choice == "3":
        print(f"Card owner: {card.owner}")
        print(f"Current balance: ¥{card.balance}")
    elif choice == "4":
        print("Thank you for using the transit card!")
        break
    else:
        print("Invalid option. Please try again.")