from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"
PASS_FILE = "passwords.txt"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def add_password(fer):
    print("\n--- Add New Password ---")
    account = input("Enter account name: ")
    password = input("Enter password: ")

    encrypted = fer.encrypt(password.encode())

    with open(PASS_FILE, "ab") as f:
        f.write(account.encode() + b" | " + encrypted + b"\n")

    print("\nPassword saved successfully ✅")

def view_passwords(fer):
    print("\n--- Saved Passwords ---")

    if not os.path.exists(PASS_FILE):
        print("No passwords found.")
        return

    with open(PASS_FILE, "rb") as f:
        for line in f:
            account, encrypted = line.split(b" | ")
            print("-------------------------")
            print(f"Account : {account.decode()}")
            print(f"Password: {fer.decrypt(encrypted).decode()}")
            print("-------------------------")

def main():
    if not os.path.exists(KEY_FILE):
        generate_key()

    fer = Fernet(load_key())

    while True:
        print("\n=============================")
        print("      PASSWORD MANAGER")
        print("=============================")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            add_password(fer)
        elif choice == "2":
            view_passwords(fer)
        elif choice == "3":
            print("\nExiting Password Manager...")
            print("Thank you for using the program 👋")
            break
        else:
            print("\nInvalid choice! Try again.")

if __name__ == "__main__":
    main()
