import tkinter as tk
from tkinter import messagebox


class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def calculate_interest(self, rate, years):
        interest = self.balance * rate * years
        return interest


class BankAccountGUI:
    def __init__(self, master):
        self.master = master
        self.accounts = {"user1": BankAccount(1000.0), "user2": BankAccount(500.0)}

        self.login_frame = tk.Frame(master)
        self.login_label = tk.Label(self.login_frame, text="Login:")
        self.login_label.pack(side=tk.LEFT)
        self.login_entry = tk.Entry(self.login_frame)
        self.login_entry.pack(side=tk.LEFT)
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(side=tk.LEFT)
        self.login_frame.pack()

    def login(self):
        username = self.login_entry.get()
        if username in self.accounts:
            self.login_frame.pack_forget()
            self.account_gui = tk.Frame(self.master)
            self.account_gui.pack()

            self.balance_label = tk.Label(self.account_gui, text="Current Balance: ${:.2f}".format(
                self.accounts[username].check_balance()))
            self.balance_label.pack()

            self.deposit_frame = tk.Frame(self.account_gui)
            self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:")
            self.deposit_label.pack(side=tk.LEFT)
            self.deposit_entry = tk.Entry(self.deposit_frame)
            self.deposit_entry.pack(side=tk.LEFT)
            self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=lambda: self.deposit(username))
            self.deposit_button.pack(side=tk.LEFT)
            self.deposit_frame.pack()

            self.withdraw_frame = tk.Frame(self.account_gui)
            self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:")
            self.withdraw_label.pack(side=tk.LEFT)
            self.withdraw_entry = tk.Entry(self.withdraw_frame)
            self.withdraw_entry.pack(side=tk.LEFT)
            self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw",
                                             command=lambda: self.withdraw(username))
            self.withdraw_button.pack(side=tk.LEFT)
            self.withdraw_frame.pack()

            self.check_balance_button = tk.Button(self.account_gui, text="Check Balance",
                                                  command=lambda: self.check_balance(username))
            self.check_balance_button.pack()

            self.interest_frame = tk.Frame(self.account_gui)
            self.interest_rate_label = tk.Label(self.interest_frame, text="Interest Rate (e.g., 0.05 for 5%):")
            self.interest_rate_label.pack(side=tk.LEFT)
            self.interest_rate_entry = tk.Entry(self.interest_frame)
            self.interest_rate_entry.pack(side=tk.LEFT)
            self.interest_years_label = tk.Label(self.interest_frame, text="Years:")
            self.interest_years_label.pack(side=tk.LEFT)
            self.interest_years_entry = tk.Entry(self.interest_frame)
            self.interest_years_entry.pack(side=tk.LEFT)
            self.interest_button = tk.Button(self.interest_frame, text="Calculate Interest",
                                             command=lambda: self.calculate_interest(username))
            self.interest_button.pack(side=tk.LEFT)
            self.interest_frame.pack()

            self.login_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid username!")

    def deposit(self, username):
        amount = float(self.deposit_entry.get())
        self.accounts[username].deposit(amount)
        self.balance_label.config(text="Current Balance: ${:.2f}".format(self.accounts[username].check_balance()))
        self.deposit_entry.delete(0, tk.END)

    def withdraw(self, username):
        amount = float(self.withdraw_entry.get())
        try:
            self.accounts[username].withdraw(amount)
            self.balance_label.config(text="Current Balance: ${:.2f}".format(self.accounts[username].check_balance()))
            self.withdraw_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def check_balance(self, username):
        messagebox.showinfo("Balance", "Current Balance: ${:.2f}".format(self.accounts[username].check_balance()))

    def calculate_interest(self, username):
        rate = float(self.interest_rate_entry.get())
        years = float(self.interest_years_entry.get())
