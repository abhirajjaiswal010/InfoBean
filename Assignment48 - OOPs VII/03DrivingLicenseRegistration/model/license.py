class Person:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def check_eligibility(self):

        if self.age < 0:
            raise InvalidAgeForDrivingLicenseException("Invalid Age")

        if self.age < 18:
            raise InvalidAgeForDrivingLicenseException(
                "Age Should Be More Than 18 Years Old"
            )

    def validate_mark(self):
        if self.mark < 0 or self.mark > 100:
            raise InvalidMarkForDrivingLicenseException("Invalid Mark")
        if self.mark < 80:
            raise InvalidMarkForDrivingLicenseException("Marks Should Be More Than 80")


class InvalidAgeForDrivingLicenseException(Exception):
    pass


class InvalidMarkForDrivingLicenseException(Exception):
    pass
