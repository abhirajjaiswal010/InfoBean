'''
Assignment 2 – Vehicle Rental System

Create a parent class Vehicle with:

vehicle_no
brand
rent_per_day

Create two child classes:

Car
Bike


Requirements
Take vehicle details and number of rental days from the user.
Use super() to initialize common attributes.
Create a method calculate_rent(days) in the parent class.
Override the method in both child classes.
For a Car, add ₹500 service charge to the rental amount.
For a Bike, add ₹200 service charge.
Display the final rental amount.
Sample Input
Enter Vehicle Number: MP09AB1234
Enter Brand: Honda
Enter Rent Per Day: 800
Enter Number of Days: 3
Enter Vehicle Type: Car
Expected Output
----- Rental Details -----
Vehicle Number : MP09AB1234
Brand          : Honda
Rent Per Day   : 800
Number of Days : 3
Vehicle Type   : Car
Rental Amount  : 2400
Service Charge : 500
Final Amount   : 2900
'''




from rich.prompt import Prompt


class Vehicle:
    def __init__(self, vehicle_no,brand,rent_per_day):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.rent_per_day = rent_per_day

    def calculate_rent(self):
        return 0

    def display(self):

        print("----- Vehicle Details -----")
        print("Vehicle No.   :", self.vehicle_no)
        print("brand         :", self.brand)
        print("rent_per_day  :", self.rent_per_day)


class Car(Vehicle):
    def __init__(self, vehicle_no, brand, rent_per_day):
        super().__init__(vehicle_no,brand, rent_per_day)

    def calculate_rent(self):
        service=500
        return self.rent_per_day*self.Nu

    def display(self):
        super().display()
        service = self.calculate_rent()      

        print("Vehicle Type    : Car")
        print("Serivce Charge  : 500", )
        print("Final Amount  :", service)


class Bike(Vehicle):
    def __init__(self, vehicle_no,brand, rent_per_day):
        super().__init__(vehicle_no, brand, rent_per_day)

    def calculate_rent(self):
        return self.rent_per_day*200

    def display(self):
        super().display()
        service = self.calculate_rent()      

        print("Vehicle Type    : Bike")
        print("Serivce Charge  : 200", )
        print("Final Amount  :", service)


Vehicle_no = input("Enter Vehicle No. : ")
brand = input("Enter Brand : ")
rent_per_day = int(input("Rent Per Day : "))

print("Choose Vehicle Type")
print("1.Car")
print("2.Bike")

choice = Prompt.ask("Choose Number", choices=["1", "2"])


if choice == "1":
    car = Car(Vehicle_no, brand, rent_per_day)
    car.display()
else:
    bike = Bike(Vehicle_no, brand, rent_per_day)
    bike.display()

