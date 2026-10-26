"""
Scenario 5: Ride Hailing App
📋 Problem
A ride-hailing app has two types of vehicles: Car and Bike. 
The dispatcher will enter the live trip into the terminal, 
and each vehicle type must know how to calculate the fare - it's not optional, it's a rule. 
If a developer forgets to write the fare calculation, Python will have to block it.
This scenario is a bit special, because in the previous four scenarios we learned how to create classes, 
protect data, reuse code, and get different behaviors with the same method name. 
But one big question still remains: what happens if a teammate Scooteradds a new vehicle type (say ) 
and forgets calculate_fareto write it? Will it throw an error at runtime, or will it silently calculate the wrong fare? 
Abstraction answers exactly this question - it tells Python "You have to follow this rule, or I won't let you create the object."

Requirement:
Car.calculate_fare(distance_km)= ¥400 base + ¥100/km.
Bike.calculate_fare(distance_km)= ¥150 base + ¥50/km.
The dispatcher will enter the trips one by one, donetyping to stop.

Rewrite the terminal loop in Scenario 5 so that the same loop iteration start_tripis called 
as soon as the distance is asked, _pending_distancerather than storing it and looping again at the end. 
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, driver_name):
        self.driver_name = driver_name
    @abstractmethod
    def calculate_fare(self, distance):
        pass
    def start_trip(self, distance):
        fare = self.calculate_fare(distance)
        print("\n--- Trip Details ---")
        print(f"Driver Name: {self.driver_name}")
        print(f"Trip Distance: {distance} km")
        print(f"Total Fare: {fare:.2f} yen")
class Car(Vehicle):
    def calculate_fare(self, distance):
        return 400 + (100 * distance)
class Bike(Vehicle):
    def calculate_fare(self, distance):
        return 150 + (50 * distance)
def main():
    while True:
        vehicle_type = input(
            "\nChoose vehicle (car/bike) or 'done' to exit: "
        ).strip().lower()
        if vehicle_type == "done":
            print("Ride-hailing app closed.")
            break
        if vehicle_type == "car":
            vehicle_class = Car
        elif vehicle_type == "bike":
            vehicle_class = Bike
        else:
            print("Invalid vehicle type. Choose car or bike.")
            continue
        driver_name = input("Enter driver name: ").strip()
        if not driver_name:
            print("Driver name cannot be empty.")
            continue
        try:
            distance = float(input("Enter distance (km): "))
            if distance <= 0:
                print("Distance must be greater than zero.")
                continue
            vehicle = vehicle_class(driver_name)
            vehicle.start_trip(distance)
        except ValueError:
            print("Please enter a valid number for distance.")
if __name__ == "__main__":
    main()

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, driver_name):
        self.driver_name = driver_name

    @abstractmethod
    def calculate_fare(self, distance_km):
        pass

    def start_trip(self, distance_km):
        fare = self.calculate_fare(distance_km)
        print(f"Driver {self.driver_name} - Trip fare: ¥{fare}")


class Car(Vehicle):
    def calculate_fare(self, distance_km):
        return 400 + (distance_km * 100)   # ¥400 base + ¥100/km


class Bike(Vehicle):
    def calculate_fare(self, distance_km):
        return 150 + (distance_km * 50)    # ¥150 base + ¥50/km


def main():
    trips = []

    while True:
        vehicle_type = input("Vehicle type (car/bike, or 'done' to finish): ")
        if vehicle_type == "done":
            break

        driver_name = input("Driver name: ")
        distance_km = int(input("Distance (km): "))

        if vehicle_type == "car":
            trips.append(Car(driver_name))
        elif vehicle_type == "bike":
            trips.append(Bike(driver_name))
        else:
            print("Unknown vehicle type, skipping.")
            continue

        trips[-1]._pending_distance = distance_km

    for trip in trips:
        trip.start_trip(trip._pending_distance)


if __name__ == "__main__":
    main()
"""