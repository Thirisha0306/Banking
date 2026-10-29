class BankAccount:

  def __init__(self, initial_balance=0.0):
    self.balance = initial_balance

  def check_balance(self):
    print(f"\n[Balance] Current Account Balance: ${self.balance:.2f}")

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(
          f"\n[Deposit] Successfully deposited ${amount:.2f}. New Balance:"
          f" ${self.balance:.2f}"
      )
    else:
      print("\n[Error] Deposit amount must be greater than zero.")


def main():
  account = BankAccount(100.0)  

  while True:
    print("\n--- Simple Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
      account.check_balance()
    elif choice == "2":
      try:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
      except ValueError:
        print("\n[Error] Please enter a valid number.")
    elif choice == "3":
      print("\nThank you for using the banking application. Goodbye!")
      break
    else:
      print("\n[Error] Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
  main()
