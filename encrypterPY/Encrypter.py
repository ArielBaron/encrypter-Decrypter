import os
import random

# Function to clear the VS Code terminal screen
def clear_screen():
    # ANSI escape code to clear the screen
    print("\033[H\033[J", end='')

# Clear the VS Code terminal screen

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
# Constants

Ey_RESULT_PATH = r"C:\Users\MICHA\OneDrive\שולחן העבודה\encrypterPY\Encrypted Files"
Dy_RESULT_PATH = r"C:\Users\MICHA\OneDrive\שולחן העבודה\encrypterPY\Decrypted Files"
MAIN_PREFIX = [r"C:\Users\MICHA\OneDrive\שולחן העבודה\encrypterPY\FileForDorE",r".txt"]
E_PREFIX = [r"C:\Users\MICHA\OneDrive\שולחן העבודה\encrypterPY\Encrypted Files",r".txt"]

while True:
    while True:
        try:
            choice = int(input("Pick folder: (MAIN : 0 Encrypted : 1) = "))
            PREFIX = [MAIN_PREFIX,E_PREFIX][choice]
            break
        except (TypeError, IndexError,ValueError):
            print("INVALID CHOICE")
    while True:
        FILE_NAME = input("Enter File Name: ")
        print(FILE_PATH)
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                text = f.read()
                break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
        except Exception as e:
            print("An error occurred:", e)
    while True:
        D_or_E =  input("Choose mode (E:1, D:2): ")
        if D_or_E in "1E" or D_or_E in "2D":
            break
    if D_or_E in '1E':
        key = random.randint(1, 110000)

        ENCRYPTED_FILE_PATH = Ey_RESULT_PATH + '\\' + FILE_NAME + "(E)" + PREFIX[1]  # Specify encrypted file path
        # Folder path
        folder_path = E_PREFIX[0]
        # File name to check
        file_name = FILE_NAME+PREFIX[1]

        # Combine folder path and file name to create the file path
        file_path = os.path.join(folder_path, file_name)

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)  # Remove the existing file
        with open(ENCRYPTED_FILE_PATH, 'w', encoding='utf-8') as f:  # Open encrypted file for writing with utf-8 encoding
            encrypted_text = caesar_encrypt(text, key)
            f.write(encrypted_text)
        print("Encrypted file created successfully. KEY =", key)
    elif D_or_E in "2D":
        SECRET_KEY = int(input("Enter Secret key: "))
        DECRYPTED_FILE_PATH = Dy_RESULT_PATH + '\\' + FILE_NAME + "(D)" + PREFIX[1]  # Specify decrypted file path
        with open(DECRYPTED_FILE_PATH, 'w', encoding='utf-8') as f:  # Open decrypted file for writing with utf-8 encoding
            decrypted_text = caesar_decrypt(text, SECRET_KEY)
            f.write(decrypted_text)
        print("Decrypted file created successfully.")