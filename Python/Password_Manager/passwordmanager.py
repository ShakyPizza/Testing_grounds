import os
import json
from cryptography.fernet import Fernet

def load_key():
    """Load the encryption key from a file or generate a new one."""
    print("Loading encryption key...")
    if not os.path.exists("key.key"):
        print("Key file not found. Generating a new key...")
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        print("Key file found. Loading key...")
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    print("Key loaded successfully.")
    return key

def encrypt_data(data, key):
    """Encrypt the data."""
    print("Encrypting data...")
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    print("Data encrypted successfully.")
    return encrypted

def decrypt_data(data, key):
    """Decrypt the data."""
    print("Decrypting data...")
    f = Fernet(key)
    decrypted = f.decrypt(data).decode()
    print("Data decrypted successfully.")
    return decrypted

def save_passwords(passwords, key):
    """Save passwords to an encrypted file."""
    print("Saving passwords to file...")
    encrypted_data = encrypt_data(json.dumps(passwords), key)
    with open("passwords.json", "wb") as file:
        file.write(encrypted_data)
    print("Passwords saved successfully.")

def load_passwords(key):
    """Load passwords from an encrypted file."""
    print("Loading passwords from file...")
    if not os.path.exists("passwords.json"):
        print("No password file found. Returning empty dictionary.")
        return {}
    with open("passwords.json", "rb") as file:
        encrypted_data = file.read()
        passwords = json.loads(decrypt_data(encrypted_data, key))
    print("Passwords loaded successfully.")
    return passwords

def add_password(service, username, password, key):
    """Add a password entry."""
    print(f"Adding password for service: {service}")
    passwords = load_passwords(key)
    if service not in passwords:
        passwords[service] = []  # Initialize as a list for new services
    elif isinstance(passwords[service], dict):
        # Convert existing single entry to a list
        passwords[service] = [passwords[service]]
    passwords[service].append({"username": username, "password": password})
    save_passwords(passwords, key)
    print(f"Password for '{service}' has been added.")

def view_password(service, key):
    """View a password entry."""
    print(f"Viewing passwords for service: {service}")
    passwords = load_passwords(key)
    if service in passwords:
        print(f"Service: {service}")
        for i, entry in enumerate(passwords[service], 1):
            print(f"{i}. Username: {entry['username']}, Password: {entry['password']}")
    else:
        print(f"No entry found for service '{service}'.")

def list_services(key):
    """List all service entries."""
    print("Listing all services...")
    passwords = load_passwords(key)
    if passwords:
        for service in passwords.keys():
            print(f"Service: {service}")
    else:
        print("No entries found.")

def delete_password(service, key):
    """Delete a password entry."""
    print(f"Deleting password for service: {service}")
    passwords = load_passwords(key)
    if service in passwords:
        print(f"Service: {service}")
        for i, entry in enumerate(passwords[service], 1):
            print(f"{i}. Username: {entry['username']}, Password: {entry['password']}")
        choice = int(input("Choose a number to delete (or 0 to cancel): "))
        if 0 < choice <= len(passwords[service]):
            passwords[service].pop(choice - 1)
            if not passwords[service]:
                del passwords[service]  # Remove service if no credentials remain
            save_passwords(passwords, key)
            print(f"Entry number {choice} for '{service}' has been deleted.")
        else:
            print("Invalid choice.")
    else:
        print(f"No entry found for service '{service}'.")

def main():
    print("Starting Password Manager...")
    key = load_key()
    while True:
        print("\nPassword Manager")
        print("1. Add password")
        print("2. View password")
        print("3. Delete password")
        print("4. List services")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        print(f"User selected option: {choice}")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password, key)

        elif choice == "2":
            service = input("Enter the service name: ")
            view_password(service, key)

        elif choice == "3":
            service = input("Enter the service name: ")
            delete_password(service, key)

        elif choice == "4":
            print("Listing all services... \n")
            list_services(key)

        elif choice == "5":
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
