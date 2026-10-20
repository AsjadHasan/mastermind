"""
T2. Student hostel residents
Problem statement
A university hostel keeps a record of each resident. Every resident has a different name and room number, 
but the hostel name and the curfew time are the same for everyone.
1. Create a Resident class with class attributes hostel_name = "Rainbow Hall" and curfew = "10:00 PM".
2. The constructor takes name and room as instance attributes.
3. Create the three residents below (store them in a list) and print one line per resident with all four values.
4. The hostel then extends the curfew to 11:00 PM. Update it with one line of code so every resident sees the change, 
and print each resident's curfew again.
"""
class Resident:
    hostel_name = "Rainbow Hall"
    curfew = "10:00 PM"
    def __init__(self, name, room):
        self.name = name
        self.room = room
residents = []
number = int(input("Enter number of residents: "))
for i in range(number):
    print(f"\nResident {i + 1}")
    name = input("Enter name: ")
    room = int(input("Enter room number: "))
    resident = Resident(name, room)
    residents.append(resident)
print("\n--- Resident Information ---")
for resident in residents:
    print(
        f"{resident.name} | Room {resident.room} | "
        f"{resident.hostel_name} | Curfew {resident.curfew}"
    )
Resident.curfew = input("\nEnter new curfew: ")
print("\n--- curfew updated ---")
for resident in residents:
    print(f"{resident.name} | Curfew {resident.curfew}")