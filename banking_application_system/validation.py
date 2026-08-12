class InsufficientBalanceError(Exception):
    """
    Raised when account balance is insufficient
    for withdrawal or transfer.
    """

    def __init__(self, message="Insufficient balance in account."):
        super().__init__(message)


class InvalidAmountError(Exception):
    """
    Raised when amount is less than
    or equal to zero.
    """

    def __init__(self, message="Invalid amount entered."):
        super().__init__(message)