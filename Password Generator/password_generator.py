import random
from pathlib import Path
from cryptography.fernet import Fernet
import os

# Pathways
app_support = Path.home() / 'Library' / 'Application Support'
hidden_path = app_support / '.pw_store.dat'
key_path = app_support / '.pw_key.key'
# Ensure file exist
app_support.mkdir(parents=True, exist_ok=True)
if not hidden_path.exists():
    hidden_path.touch(mode=0o600)
else:
    os.chmod(hidden_path, 0o600)
if not key_path.exists():
    key_path.write_bytes(Fernet.generate_key())
#Loading Key
key = key_path.read_bytes()
fernet = Fernet(key)

def generateAPassword(w, x, y, z):
    startPassword = []
    if w.lower() == "true":
        startPassword += [chr(random.randint(65, 90)) for _ in range(1)]
    startPassword += [chr(random.randint(97, 122)) for _ in range(x)]
    startPassword += [chr(random.randint(48, 57)) for _ in range(y)]
    symbol_ranges = (
        list(range(33, 48)) +
        list(range(58, 65)) +
        list(range(91, 97)) +
        list(range(123, 127))
    )
    startPassword += [chr(random.choice(symbol_ranges)) for _ in range(z)]
    random.shuffle(startPassword)
    return ''.join(startPassword)

def store_password(label, password):
    combined = f"{label}:{password}"
    encrypted = fernet.encrypt(combined.encode())
    with open(hidden_path, 'ab') as f:
        f.write(encrypted + b'\n')

def read_passwords():
    print("\nStored Passwords:")
    try:
        with open(hidden_path, 'rb') as f:
            for line in f:
                try:
                    decrypted = fernet.decrypt(line.strip()).decode()
                    label, password = decrypted.split(':', 1)
                    print(f"{label}: {password}")
                except Exception:
                    print("⚠️ Could not decrypt one entry.")
    except FileNotFoundError:
        print("No password file found.")

choice = input("\nDo you want to [generate] a new password or [view] saved ones? ").strip().lower()

if choice == 'view':
    read_passwords()
elif choice == 'generate':
    print("\nWelcome to the password generator.")
    label = input("What is this password for? (e.g., GitHub, Email): ").strip()
    upper_char = input("Need a capital letter? True or False: ")
    lower_char = int(input("How many lowercase letters? "))
    number_char = int(input("How many numbers? "))
    symbol_char = int(input("How many symbols? "))

    createdPassword = generateAPassword(upper_char, lower_char, number_char, symbol_char)
    print("\nYour password is: " + createdPassword)
    store_password(label, createdPassword)
    print(f"\n🔐 Password for '{label}' stored securely.")
else:
    print("Invalid option. Please choose 'generate' or 'view'.")
