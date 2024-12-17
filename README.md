# Encrypter-Decrypter

This Python-based tool allows you to encrypt and decrypt text files using a Caesar cipher method. It provides a simple interface for securing your text data by shifting characters based on a secret key.

## Features

- **Text Encryption**: Encrypts plain text files by shifting characters using a randomly generated key.
- **Text Decryption**: Decrypts previously encrypted text files using the provided secret key.
- **Clipboard Integration**: Optionally copies decrypted text directly to your clipboard for easy access.
- **Local File Management**: Handles files within local directories, avoiding the need for absolute paths.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Required Libraries**: Install the necessary Python libraries using the following command:

  ```bash
  pip install pyperclip
  ```

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ArielBaron/encrypter-Decrypter.git
   cd encrypter-Decrypter
   ```

2. **Directory Structure**:

   The project uses the following local directories:

   - `./FileForDorE`: Main directory containing files to be encrypted.
   - `./Encrypted Files`: Directory where encrypted files are stored.
   - `./Decrypted Files`: Directory where decrypted files are stored.

   Ensure these directories exist or create them as needed.

## Usage

1. **Run the Script**:

   ```bash
   python Encrypter.py
   ```

2. **Follow the Prompts**:

   - **Select Folder**: Choose the folder containing the file you wish to process:
     - `0` for Main Directory (`./FileForDorE`)
     - `1` for Encrypted Directory (`./Encrypted Files`)

   - **Enter File Name**: Provide the name of the file to encrypt or decrypt.

   - **Choose Mode**:
     - `1` or `E` for Encryption
     - `2` or `D` for Decryption

   - **Encryption**:
     - A random key between 1 and 110,000 is generated.
     - The file is encrypted and saved in the `./Encrypted Files` directory.
     - The encryption key is displayed; **store it securely** for decryption.

   - **Decryption**:
     - Enter the secret key used during encryption.
     - The file is decrypted and saved in the `./Decrypted Files` directory.
     - Optionally, copy the decrypted text to your clipboard by responding with `y` when prompted.

## Notes

- **File Paths**: The script uses relative paths for file operations, ensuring compatibility across different systems.
- **Clipboard Functionality**: The `pyperclip` library is used for clipboard operations. Ensure it is installed and functioning on your system.
- **Security**: The Caesar cipher is a basic encryption method and may not provide strong security for sensitive data. Use with caution and consider more robust encryption methods for critical information.





