from abc import ABC, abstractmethod


class Hospital(ABC):

    def __init__(self, patient_id, patient_name, patient_age):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    def calculate_final_amount(self, bill, discount):
        self.final_amount = bill - discount
        return self.final_amount
 
    @abstractmethod
    def generate_bill(self):
        bill = self.calculate_bill()
        discount = self.calculate_discount()
        final_amount = self.calculate_final_amount(bill, discount)

        print(f"""
========================================
           HOSPITAL BILL
========================================
Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}  
Patient Age      : {self.patient_age}
Patient Type     : {self.patient_type}

Consultation Fee : Rs.{self.consultation_fee:.2f}
Room Charges     : Rs.{self.room_charge * self.number_of_days:.2f}
Medicine Charges : Rs.{self.medicine_charge:.2f}
""")

        if self.patient_type == "Emergency":
            print(f"Emergency Charge : Rs.{self.emergency_charge:.2f}\n")

        if self.patient_type == "Insurance":
            print(f"""Insurance Cover  : 70%
Insurance Amount : Rs.{discount:.2f}
""")

        elif self.patient_type == "Corporate":
            print(f"""Corporate Discount : 20%
Discount Amount    : Rs.{discount:.2f}
""")

        else:
            print(f"Discount         : Rs.{discount:.2f}\n")

        print(f"""----------------------------------------
Total Hospital Bill : Rs.{bill:.2f}
Patient Payable     : Rs.{final_amount:.2f}
Bill Status         : GENERATED
========================================
""")


class GeneralPatient(Hospital):

    def __init__(
        self, patient_id, patient_name, patient_age, number_of_days, medicine_charge
    ):
        super().__init__(patient_id, patient_name, patient_age)

        self.patient_type = "General"
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

    def calculate_bill(self):
        self.consultation_fee = 500
        self.room_charge = 1000

        self.total = (
            self.consultation_fee
            + (self.room_charge * self.number_of_days)
            + self.medicine_charge
        )

        return self.total

    def calculate_discount(self):
        return 0

    def generate_bill(self):

        super().generate_bill()


class EmergencyPatient(Hospital):

    def __init__(
        self, patient_id, patient_name, patient_age, number_of_days, medicine_charge
    ):
        super().__init__(patient_id, patient_name, patient_age)

        self.patient_type = "Emergency"
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

    def calculate_bill(self):
        self.consultation_fee = 1000
        self.room_charge = 2000
        self.emergency_charge = 500

        self.total = (
            self.consultation_fee
            + (self.room_charge * self.number_of_days)
            + self.medicine_charge
            + self.emergency_charge
        )

        return self.total

    def calculate_discount(self):
        return 0


class InsurancePatient(Hospital):

    def __init__(
        self, patient_id, patient_name, patient_age, number_of_days, medicine_charge
    ):
        super().__init__(patient_id, patient_name, patient_age)

        self.patient_type = "Insurance"
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

    def calculate_bill(self):
        self.consultation_fee = 800
        self.room_charge = 1500

        self.total = (
            self.consultation_fee
            + (self.room_charge * self.number_of_days)
            + self.medicine_charge
        )

        return self.total

    def calculate_discount(self):
        return self.calculate_bill() * 0.70


class CorporatePatient(Hospital):

    def __init__(
        self, patient_id, patient_name, patient_age, number_of_days, medicine_charge
    ):
        super().__init__(patient_id, patient_name, patient_age)

        self.patient_type = "Corporate"
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

    def calculate_bill(self):
        self.consultation_fee = 700
        self.room_charge = 1200

        self.total = (
            self.consultation_fee
            + (self.room_charge * self.number_of_days)
            + self.medicine_charge
        )

        return self.total

    def calculate_discount(self):
        return self.calculate_bill() * 0.20
