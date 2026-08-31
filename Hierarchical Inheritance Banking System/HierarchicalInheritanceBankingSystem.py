# ==================================================
# HIERARCHICAL INHERITANCE - BANK ACCOUNT
# ==================================================
#
#                 BankAccount
#                 /    |    \
#                /     |     \
#               /      |      \
#        Savings     Current    Salary
#        Account     Account    Account
#
# ==================================================


# --------------------------------------------------
# Parent Class: BankAccount
# --------------------------------------------------

class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully.")

    # Display current balance
    def display_balance(self):
        print("Current Balance: ₹", self.balance)

    # Display account details
    def account_details(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance: ₹", self.balance)


# --------------------------------------------------
# Child Class: SavingsAccount
# --------------------------------------------------

class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        interest_rate
    ):
        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.interest_rate = interest_rate

    def display_savings_details(self):
        print("Interest Rate:", self.interest_rate, "%")


# --------------------------------------------------
# Child Class: CurrentAccount
# --------------------------------------------------

class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        overdraft_limit
    ):
        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.overdraft_limit = overdraft_limit

    def display_current_details(self):
        print("Overdraft Limit: ₹", self.overdraft_limit)


# --------------------------------------------------
# Child Class: SalaryAccount
# --------------------------------------------------

class SalaryAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance,
        employer,
        monthly_salary
    ):
        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.employer = employer
        self.monthly_salary = monthly_salary

    def display_salary_details(self):
        print("Employer:", self.employer)
        print("Monthly Salary: ₹", self.monthly_salary)


# ==================================================
# Creating Multiple Objects
# ==================================================

# Savings Account objects
savings1 = SavingsAccount(
    "SA101",
    "Rahul",
    50000,
    6.5
)

savings2 = SavingsAccount(
    "SA102",
    "Priya",
    75000,
    7.0
)


# Current Account objects
current1 = CurrentAccount(
    "CA101",
    "Arjun",
    100000,
    50000
)

current2 = CurrentAccount(
    "CA102",
    "Sneha",
    150000,
    75000
)


# Salary Account objects
salary1 = SalaryAccount(
    "SAL101",
    "Vikram",
    60000,
    "Infosys",
    80000
)

salary2 = SalaryAccount(
    "SAL102",
    "Ananya",
    90000,
    "TCS",
    95000
)


# ==================================================
# Savings Account Demonstration
# ==================================================

print("\n========================================")
print("SAVINGS ACCOUNT 1")
print("========================================")

# Inherited method
savings1.account_details()

# Inherited method
savings1.deposit(10000)

# Inherited method
savings1.display_balance()

# Child-specific property
savings1.display_savings_details()


print("\n========================================")
print("SAVINGS ACCOUNT 2")
print("========================================")

savings2.account_details()
savings2.deposit(5000)
savings2.display_balance()
savings2.display_savings_details()


# ==================================================
# Current Account Demonstration
# ==================================================

print("\n========================================")
print("CURRENT ACCOUNT 1")
print("========================================")

# Inherited method
current1.account_details()

# Inherited method
current1.deposit(20000)

# Inherited method
current1.display_balance()

# Child-specific property
current1.display_current_details()


print("\n========================================")
print("CURRENT ACCOUNT 2")
print("========================================")

current2.account_details()
current2.deposit(15000)
current2.display_balance()
current2.display_current_details()


# ==================================================
# Salary Account Demonstration
# ==================================================

print("\n========================================")
print("SALARY ACCOUNT 1")
print("========================================")

# Inherited method
salary1.account_details()

# Inherited method
salary1.deposit(10000)

# Inherited method
salary1.display_balance()

# Child-specific properties
salary1.display_salary_details()


print("\n========================================")
print("SALARY ACCOUNT 2")
print("========================================")

salary2.account_details()
salary2.deposit(12000)
salary2.display_balance()
salary2.display_salary_details()
