# Initialize transactions list to store ticket bookings
transactions = []

# User credentials (username and password)
user_credentials = {"user123": "password123"}

# Variable to track the logged-in user
current_user = None

# Function to perform user login
def login():
    global current_user
    print("Please log in.")
    username = input("Username: ")
    password = input("Password: ")

    # Check if username and password match the stored credentials
    if username in user_credentials and user_credentials[username] == password:
        current_user = username
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Function to add a new ticket booking (transaction)
def add_transaction():
    if not current_user:
        print("Error: Please log in first.")
        return
    
    print("Enter the booking details:")
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description (e.g., Event Name): ")
    amount = input("Amount (Ticket Price): ")

    # Ensure all fields are filled
    if not date or not description or not amount:
        print("Error: Please enter all fields.")
        return
    
    # Ensure the amount is a valid number
    try:
        amount = float(amount)
    except ValueError:
        print("Error: Amount must be a valid number.")
        return
    
    # Add the transaction to the list
    transactions.append({"date": date, "description": description, "amount": amount})
    print("Ticket booked successfully!")

# Function to view all transactions
def view_transactions():
    if not transactions:
        print("No transactions to display.")
        return
    print("\nCurrent Transactions:")
    for transaction in transactions:
        print(f"Date: {transaction['date']}, Description: {transaction['description']}, Amount: {transaction['amount']}")
    
# Main program loop
def main():
    global current_user  # Declare current_user as global
    while True:
        print("\n===== Ticket Booking System =====")
        if current_user:
            print(f"Logged in as: {current_user}")
        else:
            print("Not logged in.")

        print("1. Login")
        print("2. Book Ticket")
        print("3. View Transactions")
        print("4. Logout")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            if login():
                continue
        elif choice == '2':
            add_transaction()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            print(f"Logging out {current_user}...")
            current_user = None  # Log out the user
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
