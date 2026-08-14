import csv
from datetime import datetime
from customers import (
    get_customer,
    check_balance,
    update_balance
)
from validation import (
    InsufficientBalanceError,
    InvalidAmountError
)

# from logger import logger

TRANSACTION_FILE = "transactions.csv"


def record_transaction(
        transaction_type,
        account_no,
        amount,
        source_account="",
        destination_account=""):
    """
    Store transaction history.
    """

    with open(TRANSACTION_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            transaction_type,
            account_no,
            source_account,
            destination_account,
            amount
        ])


def deposit(account_no, amount,logger=None):
    try:
        """
        Deposit money into account.
        """

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        customer = get_customer(account_no)

        if not customer:
            raise ValueError("Account not found.")

        new_balance = customer["balance"] + amount

        update_balance(account_no, new_balance)

        record_transaction(
            "DEPOSIT",
            account_no,
            amount
        )

        logger.info(
            f"Deposit Successful | Acc:{account_no} | Amount:{amount}"
        )

        return new_balance
    except Exception as ex:
        logger.error(f"deposit exception: {ex}")

def withdraw(account_no, amount,logger=None):
    try:
        """
        Withdraw money from account.
        """

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        customer = get_customer(account_no)

        if not customer:
            raise ValueError("Account not found.")

        balance = customer["balance"]

        if amount > balance:
            logger.error(
                f"Insufficient Balance | Acc:{account_no}"
            )

            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        new_balance = balance - amount

        update_balance(account_no, new_balance)

        record_transaction(
            "WITHDRAW",
            account_no,
            amount
        )

        logger.info(
            f"Withdrawal Successful | Acc:{account_no} | Amount:{amount}"
        )

        return new_balance
    except Exception as ex:
        logger.error(f"withdraw excpetion {ex}")


def transfer_money(
        sender_account,
        receiver_account,
        amount,
        logger=None):
    try:
        """
        Transfer money between accounts.
        """

        if amount <= 0:
            raise InvalidAmountError(
                "Transfer amount must be greater than zero."
            )

        sender = get_customer(sender_account)
        receiver = get_customer(receiver_account)

        if not sender:
            raise ValueError("Sender account not found.")

        if not receiver:
            raise ValueError("Receiver account not found.")

        if sender["balance"] < amount:

            logger.error(
                f"Transfer Failed | Sender:{sender_account}"
            )

            raise InsufficientBalanceError(
                "Insufficient balance for transfer."
            )

        sender_balance = sender["balance"] - amount
        receiver_balance = receiver["balance"] + amount

        update_balance(
            sender_account,
            sender_balance,
            logger
        )

        update_balance(
            receiver_account,
            receiver_balance,
            logger
        )

        record_transaction(
            "TRANSFER",
            sender_account,
            amount,
            sender_account,
            receiver_account
        )

        logger.info(
            f"Transfer Successful | "
            f"From:{sender_account} "
            f"To:{receiver_account} "
            f"Amount:{amount}"
        )

        return True
    except Exception as ex:
        logger.error(f"transfer_money exception {ex}")


def transaction_history(account_no,logger=None):
    """
    Display account transaction history.
    """

    history = []

    try:
        with open(TRANSACTION_FILE, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[2] == str(account_no):
                    history.append(row)

    except FileNotFoundError:
        print("No transaction history found.")
        logger.error(f"No transaction history found for the account: {account_no}.")

    return history