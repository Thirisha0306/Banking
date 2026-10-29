 def main():
    balance = 0.0

    while True:
        print("\n=== BANKING APPLICATION ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            print(f"\nYour current balance is: ${balance:.2f}")
        elif choice == '2':
            amount = float(input("\nEnter deposit amount: $"))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount:.2f}")
            else:
                print("Invalid amount. Deposit must be greater than 0.")
        elif choice == '3':
            amount = float(input("\nEnter withdrawal amount: $"))
            if amount > balance:
                print("\n Transaction Denied")
            elif amount <= 0:
                print("\n Invalid amount. Withdrawal must be greater than 0.")
            else:
                balance -= amount
                print(f"\n Successfully withdrew ${amount:.2f}")
        elif choice == '4':
            print("\nThank you" )
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



