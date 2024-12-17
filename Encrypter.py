import os
import random
import pyperclip
# Function to clear the terminal screen
def clear_screen():
    # ANSI escape code to clear the screen
    print("\033[H\033[J", end='')

# Caesar cipher functions
def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        # Apply Caesar encryption
        encrypted_char = chr((ord(char) + key) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        # Apply Caesar decryption
        decrypted_char = chr((ord(char) - key) % 256)
        decrypted_text += decrypted_char
    return decrypted_text

def delete_all_files_in_folders(folders):
    for folder in folders:
        if not os.path.exists(folder):
            print(f"Folder does not exist: {folder}")
            continue
        
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def create_dummy_data(folder, num_files=5):
    """
    Creates dummy text files with Shakespeare content in the specified folder.

    :param folder: The folder where dummy files will be created.
    :param num_files: Number of files to create (default is 5).
    """
    if not os.path.exists(folder):
        os.makedirs(folder)  # Ensure the folder exists
        print(f"Created folder: {folder}")
    
    # Sample Shakespeare passages
    shakespeare_texts = [
        "To be, or not to be, that is the question.",
        "All the world’s a stage, and all the men and women merely players.",
        "Some are born great, some achieve greatness, and some have greatness thrust upon them.",
        "The course of true love never did run smooth.",
        "If music be the food of love, play on.",
        "A fool thinks himself to be wise, but a wise man knows himself to be a fool.",
        "Brevity is the soul of wit.",
        "The lady doth protest too much, methinks.",
        "Cowards die many times before their deaths; the valiant never taste of death but once.",
        "Love looks not with the eyes, but with the mind, and therefore is winged Cupid painted blind."
    ]
    
    for i in range(1, num_files + 1):
        file_name = f"text{i}.txt"
        file_path = os.path.join(folder, file_name)

        # Select random excerpts for the file
        num_passages = random.randint(2, 5)  # Each file will have 2-5 passages
        content = "\n".join(random.choices(shakespeare_texts, k=num_passages))

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created file: {file_path}")
                    
# Constants
MAIN_DIR = "./FileForDorE"
ENCRYPTED_DIR = "./Encrypted Files"
DECRYPTED_DIR = "./Decrypted Files"

os.makedirs(MAIN_DIR, exist_ok=True)
os.makedirs(ENCRYPTED_DIR, exist_ok=True)
os.makedirs(DECRYPTED_DIR, exist_ok=True)

MAIN_PREFIX = [MAIN_DIR, ".txt"]
E_PREFIX = [ENCRYPTED_DIR, ".txt"]

# Main loop
while True:
    try:
        choice = int(input("Pick folder: (MAIN : 0 Encrypted : 1 Rest all : 2 Load Dummy data to main folder : 3) = "))
        if choice == 0 or choice == 1:
            PREFIX = [MAIN_PREFIX, E_PREFIX][choice]
        elif choice == 2:
            delete_all_files_in_folders([MAIN_DIR, ENCRYPTED_DIR, DECRYPTED_DIR])
            print("cleared all data in folders")
            exit()
        elif choice == 3:
            amount_files = int(input("amonut of files: "))
            create_dummy_data(MAIN_DIR,amount_files)
            print(f"added {amount_files} files")
            continue
        break
    except (TypeError, IndexError, ValueError):
        print("INVALID CHOICE")

while True:
    FILE_NAME = input("Enter File Name (without extension): ")
    FILE_PATH = os.path.join(PREFIX[0], FILE_NAME + PREFIX[1])  # Construct the file path
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            text = f.read()
            break
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
    except Exception as e:
        print("An error occurred:", e)

while True:
    D_or_E = input("Choose mode (E:1, D:2): ").upper()
    if D_or_E in ("1", "E", "2", "D"):
        break

if D_or_E in ('1', 'E'):
    key = random.randint(1, 110000)

    ENCRYPTED_FILE_PATH = os.path.join(ENCRYPTED_DIR, FILE_NAME  + PREFIX[1])  # Specify encrypted file path
    # Remove the existing file if it exists
    if os.path.exists(ENCRYPTED_FILE_PATH):
        os.remove(ENCRYPTED_FILE_PATH)

    with open(ENCRYPTED_FILE_PATH, 'w', encoding='utf-8') as f:  # Open encrypted file for writing
        encrypted_text = caesar_encrypt(text, key)
        f.write(encrypted_text)
    print("Encrypted file created successfully. KEY =", key, " Copied!")
    pyperclip.copy(str(key))
        
elif D_or_E in ('2', 'D'):
    SECRET_KEY = int(input("Enter Secret key: "))
    DECRYPTED_FILE_PATH = os.path.join(DECRYPTED_DIR, FILE_NAME + PREFIX[1])  # Specify decrypted file path

    with open(DECRYPTED_FILE_PATH, 'w', encoding='utf-8') as f:  # Open decrypted file for writing
        decrypted_text = caesar_decrypt(text, SECRET_KEY)
        f.write(decrypted_text)
        print("Decrypted file created successfully.")
    while True:
        copy = input("Do you want to copy the output to your clipboard? (y/n): ").lower()
        if copy == "y":
            # Open the file in read mode to fetch the content
            with open(DECRYPTED_FILE_PATH, 'r', encoding='utf-8') as f:
                pyperclip.copy(f.read())  # Copy the file content to the clipboard
            print("Decrypted content copied to clipboard.")
            break
        elif copy == "n":
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")