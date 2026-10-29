def main():
    balance = 0.0

    while True:
        print("\n BANKING APPLICATION")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")

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
            print("\nThank you for using the Banking Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



