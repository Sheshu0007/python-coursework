print(" Welcome to HDFC Bank Account System")


name = input("Enter your full name: ")
account_type = input("Enter account type (Savings/Current): ")
ifsc = input("Enter IFSC Code: ")

# Integer
account_number = int(input("Enter Account Number: "))

# Float
balance = float(input("Enter initial balance amount (₹): "))

# Boolean
is_active_input = input("Is the account active? (yes/no): ").lower()
is_active = is_active_input == "yes"

overdraft_input = input("Is overdraft allowed? (yes/no): ").lower()
overdraft = overdraft_input == "yes"

# Tuple
city = input("Enter your city: ")
state = input("Enter your state: ")
pin = input("Enter your PIN code: ")
address = (city, state, pin)

# Set
features_input = input("Enter account features (comma-separated): ")
features = set(features_input.split(","))

# dictionary to store all values
account = {
    "name": name,
    "account_type": account_type,
    "ifsc": ifsc,
    "account_number": account_number,
    "balance": balance,
    "is_active": is_active,
    "overdraft": overdraft,
    "address": address,
    "features": features
}

# Display the account summary
print(" Account Summary:")
for key, value in account.items():
    print(f"{key}: {value})")
