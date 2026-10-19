"""Module for registering courier parcels.
Problem statement-
A courier counter registers every parcel that customers drop off. 
Build a Parcel class so that each parcel object stores its own details.
1. The constructor takes sender, receiver and weight (in kg) and stores all three as instance attributes.
2. The constructor prints New parcel registered every time a parcel is created.
3. Create two parcels from the input below, then print one summary line for each.
"""

class Parcel:
    """Represent a courier parcel."""
    def __init__(self, sender, receiver, weight):
        """Initialize the parcel details and print a registration message."""
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        print("New parcel registered")
    def display_summary(self):
        """Display the parcel details."""
        print(
            f"Parcel from {self.sender} to {self.receiver}, "
            f"weight {self.weight} kg"
        )
def main():
    """Get parcel details from the user and display summaries."""
    parcels = []
    for i in range(2):
        print(f"\nEnter details for parcel {i + 1}:")
        sender = input("Enter sender name: ")
        receiver = input("Enter receiver name: ")
        weight = float(input("Enter weight (kg): "))
        parcel = Parcel(sender, receiver, weight)
        parcels.append(parcel)
    print("\nParcel Summary:")
    for parcel in parcels:
        parcel.display_summary()
if __name__ == "__main__":
    main()