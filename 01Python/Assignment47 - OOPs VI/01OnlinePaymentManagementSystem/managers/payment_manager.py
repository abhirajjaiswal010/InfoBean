class PaymentManager:
    def __init__(self):
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def find_payment(self, order_id):
        for payment in self.payments:
            if payment.order_id == order_id:
                return payment
