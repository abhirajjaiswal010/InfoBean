'''
Assignment 8: Car Mileage Calculator

A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:
- Car brand
- Car model
- Distance travelled in km
- Fuel consumed in litres
- Petrol price per litre

Create the following methods:
- calculate_mileage() – Calculate kilometres per litre.
- calculate_fuel_cost() – Calculate total fuel cost.
- display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
'''
class Car:

    def __init__(self, brand, model, distance, fuel_consumed, petrol_price):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.fuel_consumed = fuel_consumed
        self.petrol_price = petrol_price

    def calculate_mileage(self):
        return self.distance/self.fuel_consumed

    def calculate_fuel_cost(self):
        return self.fuel_consumed*self.petrol_price

    def display_trip_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Distance Travelled: {self.distance} km")
        print(f"Fuel Consumed: {self.fuel_consumed} litres")
        print(f"Petrol Price: {self.petrol_price}")
        print(f"Mileage: {self.calculate_mileage()} km/l")
        print(f"Fuel Cost: {self.calculate_fuel_cost()} rs.")


c1 = Car("Maruti", "Swift", 320, 20, 105)

c1.display_trip_details()