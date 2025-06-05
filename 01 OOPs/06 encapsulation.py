class BankAccount:
    def __init__(self):
        self.__account_holder = ""
        self.__balance = 0

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_account_holder(self):
        return self.__account_holder

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    # Setter method to modify balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")


class PaymentProcessor:
    def __init__(self, card_number, amount):
        self.__card_number = self.__mask_card_Number(card_number)
        self.__amount = amount

    def __mask_card_Number(self, card_number):
        return "****-****-****-" + card_number[-4:]

    def process_payment(self):
        print(f"Processing payment of {self.__amount} for card {self.__card_number}")


if __name__ == "__main__":
    # account = BankAccount()
    # account.set_account_holder("Arnab")
    # account.set_balance(1000)
    # print("Current balance:", account.get_balance())
    # account.deposit(100)
    # print("Current balance:", account.get_balance())

    payment = PaymentProcessor("123456789017", 250)
    payment.process_payment()
