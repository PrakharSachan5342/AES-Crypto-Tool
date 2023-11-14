###check the encrypted message 

# Read and print the numeric contents of the encrypted file
encrypted_file_path = 'cipher_cryptography project.txt'

with open(encrypted_file_path, 'rb') as encrypted_file:
    encrypted_content = encrypted_file.read()

    print("Numeric representation of the Encrypted Content:")
    for num in encrypted_content:
        print(num, end=' ')
