from cryptography.fernet import Fernet

# This block read the key and stores it in a variable
key_location = input("Enter Key filepath -> ")  # This line takes key file path.
key_in = open(key_location,'rb')    # opens file in read byte mode.
key_read = key_in.read()     # Reads key file.
key = Fernet(key_read)       # store key in key variable.
file_close = key_in.close()  # closes key file.


# This Block of code encrypts the file.
plaintext_file_name = input("Enter Plaintext filepath -> ")  # Takes plaintext filepath.

pf = open(plaintext_file_name, 'rb')   # stores whole file in enc_file variable.
enc_file = pf.read()                      # pf for plaintext file.

encrypted_file = key.encrypt(enc_file) # encrypts the file and saves it in encrypted_file variable.

# This Block of code outputs encrypted file.
of = open(plaintext_file_name + ".encrypted",'wb')  # new file with encrypted content, ending with ".encrypted" extension.
of.write(encrypted_file)                               # of for output file.
