'''
Assignment 7: Mobile Phone Data Usage

A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:
- Customer name
- Mobile number
- Total data in GB
- Used data in GB
- Validity in days

Create the following methods:
- calculate_remaining_data() – Calculate remaining data.
- calculate_usage_percentage() – Calculate the percentage of data used.
- display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%
'''
class MobilePlan:

    def __init__(self, customer_name, mobile_number, total_data, used_data, validity):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.total_data = total_data
        self.used_data = used_data
        self.validity = validity

    def calculate_remaining_data(self):
        return self.total_data-self.used_data

    def calculate_usage_percentage(self):
        
        return (self.used_data/self.total_data)*100

    def display_plan(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Mobile Number: {self.mobile_number}")
        print(f"Total Data: {self.total_data} GB")
        print(f"Used Data: {self.used_data} GB")
        print(f"Validity: {self.validity} days")
        print(f"Remaining Data: {self.calculate_remaining_data()} GB")
        print(f"Usage Percentage: {self.calculate_usage_percentage()}%")

m1 = MobilePlan("Abhiraj", 9876543210, 50, 18, 28)

m1.display_plan()