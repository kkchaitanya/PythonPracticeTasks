# ==========================================
# METHOD OVERRIDING / POLYMORPHISM
# Payment Example
# ==========================================


# ------------------------------------------
# Parent Class
# ------------------------------------------

class Payment:

    def process_payment(self, amount):
        print("Processing payment of ₹", amount)


# ------------------------------------------
# Child Class: Credit Card
# ------------------------------------------

class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print("Processing ₹", amount, "using Credit Card")


# ------------------------------------------
# Child Class: UPI
# ------------------------------------------

class UPIPayment(Payment):

    def process_payment(self, amount):
        print("Processing ₹", amount, "using UPI")


# ------------------------------------------
# Child Class: Net Banking
# ------------------------------------------

class NetBankingPayment(Payment):

    def process_payment(self, amount):
        print("Processing ₹", amount, "using Net Banking")


# ------------------------------------------
# Child Class: Wallet
# ------------------------------------------

class WalletPayment(Payment):

    def process_payment(self, amount):
        print("Processing ₹", amount, "using Wallet")


# ==========================================
# Creating Objects
# ==========================================

credit_card = CreditCardPayment()
upi = UPIPayment()
net_banking = NetBankingPayment()
wallet = WalletPayment()


# ==========================================
# Calling process_payment()
# Each child class gives a different output
# ==========================================

credit_card.process_payment(5000)

upi.process_payment(5000)

net_banking.process_payment(5000)

wallet.process_payment(5000)


# ==========================================
# Polymorphism Demonstration
# ==========================================

print("\n========== POLYMORPHISM ==========")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment(),
    WalletPayment()
]

for payment in payments:
    payment.process_payment(5000)
