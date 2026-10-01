from models.hospital import (
    Hospital,
    GeneralPatient,
    EmergencyPatient,
    CorporatePatient,
    InsurancePatient,
)

from managers.patient_manager import PatientManager


pm = PatientManager()


def primary():
    print("""
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. View Patient Bill
4. Exit
""")

    choice = int(input("Enter Choice : "))
    return choice


def secondary():
    print("""
========================================
       CHOOSE CATEGORY
========================================

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
""")

    choice = int(input("Enter Choice : "))
    return choice


def main_menu():

    while True:

        choice = primary()

        match choice:

            case 1:
                print()
                print("       REGISTER PATIENT")
                print()

                patient_id = input("Enter Patient Id : ")
                patient_name = input("Enter Patient Name : ")
                patient_age = int(input("Enter Patient Age : "))

                while True:

                    second_choice = secondary()

                    number_of_days = int(
                        input("Enter Number Of Days : ")
                    )

                    medicine_charge = int(
                        input("Enter Medicine Charge : ")
                    )

                    match second_choice:

                        case 1:
                            patient = GeneralPatient(
                                patient_id,
                                patient_name,
                                patient_age,
                                number_of_days,
                                medicine_charge,
                            )

                            pm.add_patient(patient)
                            print("General Patient Registered Successfully")
                            break

                        case 2:
                            patient = EmergencyPatient(
                                patient_id,
                                patient_name,
                                patient_age,
                                number_of_days,
                                medicine_charge,
                            )

                            pm.add_patient(patient)
                            print("Emergency Patient Registered Successfully")
                            break

                        case 3:
                            patient = InsurancePatient(
                                patient_id,
                                patient_name,
                                patient_age,
                                number_of_days,
                                medicine_charge,
                            )

                            pm.add_patient(patient)
                            print("Insurance Patient Registered Successfully")
                            break

                        case 4:
                            patient = CorporatePatient(
                                patient_id,
                                patient_name,
                                patient_age,
                                number_of_days,
                                medicine_charge,
                            )

                            pm.add_patient(patient)
                            print("Corporate Patient Registered Successfully")
                            break

                        case _:
                            print("Enter Valid Option")

            case 2:
                print()
                print("       VIEW PATIENT BILL")
                print()

                patient_id_search = input(
                    "Enter Patient Id : "
                )

                patient = pm.search_patient(patient_id_search)

                if patient:
                    patient.generate_bill()
                else:
                    print("Patient Not Found")

            

            case 4:
                print()
                print("Exiting...")
                print("Thanks For Using")
                break

            case _:
                print("Invalid Choice")


main_menu()