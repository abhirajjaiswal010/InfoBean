from models.payment import (
    UPIPayment,
    CreditCardPayment,
    DebitCardPayment,
    NetBankingPayment,
    WalletPayment,
)

from managers.payment_manager import PaymentManager

payment_manager = PaymentManager()


def mainDisplay():
    print("""========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit""")


def secondDisplay():
    print("""Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet""")


def main_menu():

    while True:

        mainDisplay()

        MainChoice = int(input("Enter Choice : "))

        match MainChoice:

            case 1:

                customer_name = input("Enter Customer Name : ")
                order_id = input("Enter Order ID : ")
                order_amount = float(input("Enter Order Amount : "))

                while True:

                    secondDisplay()

                    SecondChoice = int(input("Enter Choice : "))

                    match SecondChoice:

                        case 1:
                            print("UPI METHOD")

                            upi_id = input("Enter UPI ID : ")
                            upi_pin = input("Enter UPI Pin : ")

                            payment = UPIPayment(
                                customer_name, order_id, order_amount, upi_id, upi_pin
                            )
                            payment.validate_payment()
                            payment.authenticate_payment()
                            payment.process_payment()
                            payment.generate_receipt()
                            payment_manager.add_payment(payment)

                            break

                        case 2:
                            print("CREDIT CARD METHOD")

                            card_number = input("Enter Card Number : ")
                            card_holder_name = input("Enter Card Holder Name : ")
                            cvv = input("Enter CVV : ")
                            expiry_date = input("Enter Expiry Date : ")
                            payment = CreditCardPayment(
                                customer_name,
                                order_id,
                                order_amount,
                                card_number,
                                card_holder_name,
                                cvv,
                                expiry_date,
                            )
                            payment.validate_payment()
                            payment.authenticate_payment()
                            payment.process_payment()
                            payment.generate_receipt()
                            payment_manager.add_payment(payment)

                            break

                        case 3:
                            print("DEBIT CARD METHOD")

                            card_number = input("Enter Card Number : ")
                            card_holder_name = input("Enter Card Holder Name : ")
                            cvv = input("Enter CVV : ")
                            expiry_date = input("Enter Expiry Date : ")
                            payment = DebitCardPayment(
                                customer_name,
                                order_id,
                                order_amount,
                                card_number,
                                card_holder_name,
                                cvv,
                                expiry_date,
                            )
                            payment.validate_payment()
                            payment.authenticate_payment()
                            payment.process_payment()
                            payment.generate_receipt()
                            payment_manager.add_payment(payment)

                            break

                        case 4:
                            print("NET BANKING METHOD")

                            bank_name = input("Enter Bank Name : ")
                            account_number = int(input("Enter Account Number : "))
                            customer_id = input("Enter Customer ID : ")
                            payment = NetBankingPayment(
                                customer_name,
                                order_id,
                                order_amount,
                                bank_name,
                                account_number,
                                customer_id,
                            )
                            payment.validate_payment()
                            payment.authenticate_payment()
                            payment.process_payment()
                            payment.generate_receipt()
                            payment_manager.add_payment(payment)

                            break

                        case 5:
                            print("WALLET METHOD")

                            wallet_name = input("Enter Wallet Name : ")
                            mobile_number = input("Enter Mobile Number : ")
                            wallet_pin = input("Enter Wallet PIN : ")
                            payment = WalletPayment(
                                customer_name,
                                order_id,
                                order_amount,
                                wallet_name,
                                mobile_number,
                                wallet_pin,
                            )
                            payment.validate_payment()
                            payment.authenticate_payment()
                            payment.process_payment()
                            payment.generate_receipt()
                            payment_manager.add_payment(payment)

                            break

                        case _:
                            print("Invalid Payment Method")

            case 2:
                print("View Payment Details")
                print()

                order_id = input("Enter Order Id : ")
                payment = payment_manager.find_payment(order_id)

                if payment:
                    payment.generate_receipt()
                else:
                    print("Payment Record Not Found")

            case 3:
                print("Exiting")
                break

            case _:
                print("Invalid Choice")
