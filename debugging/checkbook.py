#!/usr/bin/python3
"""
Simple checkbook application.

This module provides a Checkbook class to manage a basic bank account with
deposit, withdrawal and balance display operations. It also includes a
command-line interface to interact with the checkbook.
"""


class Checkbook:
    """
    A simple checkbook to track a balance and perform operations.

    Attributes:
        balance (float): Current amount of money in the checkbook.
    """

    def __init__(self):
        """
        Initialize a new Checkbook instance.

        Sets the starting balance to 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
            amount (float): The amount of money to add to the balance.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds are available.

        Parameters:
            amount (float): The amount of money to withdraw from the balance.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Run the interactive checkbook program.

    Allows the user to deposit, withdraw, check balance or exit.
    Handles invalid numeric input to prevent the program from crashing.
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        )
        action = action.lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            amount_str = input("Enter the amount to deposit: $")
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue

            if amount <= 0:
                print("Amount must be a positive number.")
                continue

            cb.deposit(amount)

        elif action == 'withdraw':
            amount_str = input("Enter the amount to withdraw: $")
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue

            if amount <= 0:
                print("Amount must be a positive number.")
                continue

            cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
