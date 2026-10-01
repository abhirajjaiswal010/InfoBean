from abc import ABC, abstractmethod


class Payment(ABC):

    TRANSACTION_COUNTER = 1000

    def __init__(self, customer_name, order_id, order_amount):
        self.customer_name = customer_name
        self.order_id = order_id
        self.order_amount = order_amount
        self.payment_status = "PENDING"
        self.transaction_id = None

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def calculate_processing_fee(self):
        pass

    @abstractmethod
    def authenticate_payment(self):
        pass

    
    def process_payment(self):
        print("Processing payment...")
        print("Payment processed successfully.")

        Payment.TRANSACTION_COUNTER += 100
        self.transaction_id = "TXN"+str(Payment.TRANSACTION_COUNTER)
        self.payment_status = "SUCCESS"

    def generate_receipt(self):
        processing_fee = self.calculate_processing_fee()
        final_amount = self.order_amount + processing_fee

        print()        
        print("          PAYMENT RECEIPT")
        print()
        

        print(f"Customer Name   : {self.customer_name}")
        print(f"Order ID        : {self.order_id}")
        print(f"Payment Method  : {self.payment_method}")
        print(f"Order Amount    : Rs.{self.order_amount:.2f}")
        print(f"Processing Fee  : Rs.{processing_fee:.2f}")
        print(f"Final Amount    : Rs.{final_amount:.2f}")
        print(f"Transaction ID  : {self.transaction_id}")
        print(f"Payment Status  : {self.payment_status}")
        print()

        


class UPIPayment(Payment):

    def __init__(self, customer_name, order_id, order_amount, upi_id, upi_pin):

        super().__init__(customer_name, order_id, order_amount)

        self.upi_id = upi_id
        self.upi_pin = upi_pin
        self.payment_method = "UPI"

    def validate_payment(self):
        print("Validating payment details...")
        print("Payment details validated successfully.")

    def calculate_processing_fee(self):
        return self.order_amount * 0 / 100  

    def authenticate_payment(self):
        print("Authenticating payment...")
        print("Authentication successful.")

    

    


class CreditCardPayment(Payment):

    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        card_number,
        card_holder_name,
        cvv,
        expiry_date,
    ):

        super().__init__(customer_name, order_id, order_amount)

        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.payment_method = "Credit Card"

    def validate_payment(self):
        print("Validating payment details...")
        print("Payment details validated successfully.")

    def calculate_processing_fee(self):
        return self.order_amount * 2 / 100

    def authenticate_payment(self):
        print("Authenticating payment...")
        print("Authentication successful.")


class DebitCardPayment(Payment):

    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        card_number,
        card_holder_name,
        cvv,
        expiry_date,
    ):

        super().__init__(customer_name, order_id, order_amount)

        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.payment_method = "Debit Card"

    def validate_payment(self):
        print("Validating Debit Card payment details...")
        print("Payment details validated successfully.")

    def calculate_processing_fee(self):
        return self.order_amount * 1 / 100

    def authenticate_payment(self):
        print("Authenticating Debit Card payment...")
        print("Authentication successful.")


class NetBankingPayment(Payment):

    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        bank_name,
        account_number,
        customer_id,
    ):

        super().__init__(customer_name, order_id, order_amount)

        self.bank_name = bank_name
        self.account_number = account_number
        self.customer_id = customer_id
        self.payment_method = "Net Banking"

    def validate_payment(self):
        print("Validating Net Banking payment details...")
        print("Payment details validated successfully.")

    def calculate_processing_fee(self):
        return self.order_amount * 0.5 / 100

    def authenticate_payment(self):
        print("Authenticating Net Banking payment...")
        print("Authentication successful.")


class WalletPayment(Payment):

    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        wallet_name,
        mobile_number,
        wallet_pin,
    ):

        super().__init__(customer_name, order_id, order_amount)

        self.wallet_name = wallet_name
        self.mobile_number = mobile_number
        self.wallet_pin = wallet_pin
        self.payment_method = "Wallet"

    def validate_payment(self):
        print("Validating Wallet payment details...")
        print("Payment details validated successfully.")

    def calculate_processing_fee(self):
        return self.order_amount * 1.5 / 100

    def authenticate_payment(self):
        print("Authenticating Wallet payment...")
        print("Authentication successful.")
