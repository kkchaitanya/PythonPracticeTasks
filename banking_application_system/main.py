from logger import setup_logger
from customers import (
    create_account,
    check_balance
)

from transactions import (
    deposit,
    withdraw,
    transfer_money,
    transaction_history
)

from validation import (
    InvalidAmountError,
    InsufficientBalanceError
)


def show_menu():
    print("\n===== MINI BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")


while True:
    logger = setup_logger("banking_application.log")
    show_menu()

    try:
        choice = int(input("Enter your choice: "))

        # CREATE ACCOUNT
        if choice == 1:

            name = input("Enter Customer Name: ")

            balance = float(
                input("Enter Initial Deposit: ")
            )

            account_no = create_account(
                name,
                balance,
                logger
            )

            print(
                f"Account Created Successfully!"
            )

            print(
                f"Your Account Number: {account_no}"
            )

        # DEPOSIT
        elif choice == 2:

            account_no = input(
                "Enter Account Number: "
            )

            amount = float(
                input("Enter Deposit Amount: ")
            )

            balance = deposit(
                account_no,
                amount,
                logger
            )

            print(
                f"Deposit Successful."
            )

            print(
                f"New Balance: ₹{balance}"
            )

        # WITHDRAW
        elif choice == 3:

            account_no = input(
                "Enter Account Number: "
            )

            amount = float(
                input("Enter Withdrawal Amount: ")
            )

            balance = withdraw(
                account_no,
                amount,
                logger
            )

            print(
                f"Withdrawal Successful."
            )

            print(
                f"New Balance: ₹{balance}"
            )

        # TRANSFER
        elif choice == 4:

            sender = input(
                "Enter Sender Account Number: "
            )

            receiver = input(
                "Enter Receiver Account Number: "
            )

            amount = float(
                input("Enter Amount: ")
            )

            transfer_money(
                sender,
                receiver,
                amount,
                logger
            )

            print(
                "Transfer Successful."
            )

        # CHECK BALANCE
        elif choice == 5:

            account_no = input(
                "Enter Account Number: "
            )

            balance = check_balance(
                account_no
            )

            if balance is not None:
                print(
                    f"Available Balance: ₹{balance}"
                )
            else:
                print(
                    "Account Not Found"
                )

        # TRANSACTION HISTORY
        elif choice == 6:

            account_no = input(
                "Enter Account Number: "
            )

            history = transaction_history(
                account_no
            )

            if history:

                print(
                    "\n===== TRANSACTION HISTORY ====="
                )

                for transaction in history:
                    print(transaction)

            else:
                print(
                    "No Transactions Found."
                )

        # EXIT
        elif choice == 7:

            print(
                "Thank You For Using Banking System."
            )
            break

        else:
            print(
                "Invalid Choice. Try Again."
            )

    except InvalidAmountError as e:
        print("Error:", e)

    except InsufficientBalanceError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print(
            "Unexpected Error:",
            e
        )