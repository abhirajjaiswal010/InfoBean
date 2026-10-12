from model.license import (
    Person,
    InvalidAgeForDrivingLicenseException,
    InvalidMarkForDrivingLicenseException,
)

name = input("Enter Name : ")
age = int(input("Enter Age : "))
mark = int(input("Enter Mark : "))


p1 = Person(name, age, mark)


try:
    p1.check_eligibility()
    p1.validate_mark()
except InvalidMarkForDrivingLicenseException as e:
    print(f"Exception :{e}")
except InvalidAgeForDrivingLicenseException as e:
    print(f"Exception: {e}")

else:
    print("Approve For License")
