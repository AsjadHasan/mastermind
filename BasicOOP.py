"Q1. Your First Class"

class Konbini:
    name = "FamilyMart"
shop = Konbini()
print(shop.name)

"Q2. Constructor Practice"

class Employee:
    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage
Yuki = Employee("Yuki", 1200)
Kenta = Employee("Kenta", 1400)
print(f"Name: {Yuki.name}")
print(f"Hourly Wage: {Yuki.hourly_wage} yen")
print(f"Name: {Kenta.name}")
print(f"Hourly Wage: {Kenta.hourly_wage} yen")

"Q3. Class with a Method"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        area = self.width * self.height
        print(f"Rectangle area: {area}")
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)
rectangle1.get_area()
rectangle2.get_area()

"Q4. Konbini Item with Discount"

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percent):
        discount = self.price * percent / 100
        final_price = self.price - discount
        print(f"{self.name} after {percent}% discount: {final_price:.0f} yen")
item1 = Item("Onigiri", 120)
item2 = Item("Bento", 600)
item1.apply_discount(20)
item2.apply_discount(15)

"Q5. Multiple Objects + Method"

class Employee:
    def __init__(self, name, hours_worked_list):
        self.name = name
        self.hours_worked_list = hours_worked_list
    def get_total_hours(self):
        total = sum(self.hours_worked_list)
        print(f"Hi {self.name}, your total working hours: {total}")
employee1 = Employee("Yuki", [8, 7, 9, 8, 6])
employee2 = Employee("Kenta", [7, 8, 8, 9, 7])
employee3 = Employee("Tanaka", [8, 8, 8, 8, 8])
employee4 = Employee("Asjad", [9, 8, 7, 8, 6])
employee1.get_total_hours()
employee2.get_total_hours()
employee3.get_total_hours()
employee4.get_total_hours()