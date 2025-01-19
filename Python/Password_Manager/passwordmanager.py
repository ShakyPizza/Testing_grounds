import os
import json
from cryptography.fernet import Fernet

def load_key():
    """Load the encryption key from a file or generate a new one."""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

def encrypt_data(data, key):
    """Encrypt the data."""
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(data, key):
    """Decrypt the data."""
    f = Fernet(key)
    return f.decrypt(data).decode()

def save_passwords(passwords, key):
    """Save passwords to an encrypted file."""
    encrypted_data = encrypt_data(json.dumps(passwords), key)
    with open("passwords.json", "wb") as file:
        file.write(encrypted_data)

def load_passwords(key):
    """Load passwords from an encrypted file."""
    if not os.path.exists("passwords.json"):
        return {}
    with open("passwords.json", "rb") as file:
        encrypted_data = file.read()
        return json.loads(decrypt_data(encrypted_data, key))

def add_password(service, username, password, key):
    """Add a password entry."""
    passwords = load_passwords(key)
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords, key)
    print(f"Password for '{service}' added successfully.")

def view_password(service, key):
    """View a password entry."""
    passwords = load_passwords(key)
    if service in passwords:
        entry = passwords[service]
        print(f"Service: {service}\nUsername: {entry['username']}\nPassword: {entry['password']}")
    else:
        print(f"No entry found for service '{service}'.")

def list_services(key):
    """List all services entries."""
    passwords = load_passwords(key)
    if passwords:
        for service in passwords.keys():
            print(f"Service: {service}")
    else:
        print("No services entries found.")

def delete_password(service, key):
    """Delete a password entry."""
    passwords = load_passwords(key)
    if service in passwords:
        del passwords[service]
        save_passwords(passwords, key)
        print(f"Password for '{service}' deleted successfully.")
    else:
        print(f"No entry found for service '{service}'.")

def main():
    key = load_key()
    while True:
        print("\nPassword Manager")
        print("1. Add password")
        print("2. View password")
        print("3. Delete password")
        print("4. List services")
        print("5. Quit")
        
        choice = input("Enter your choice: ")

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
            print("Printing list of services... \n")
            list_services(key)

        elif choice == "5":
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
