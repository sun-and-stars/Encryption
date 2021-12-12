from cryptography.fernet import Fernet

# This block read the key and stores it in a variable
key_location = input("Enter Key filepath -> ")  # This line takes key file path.
key_in = open(key_location,'rb')    # opens file in read byte mode.
key_read = key_in.read()     # Reads key file.
key = Fernet(key_read)       # store key in key variable.
file_close = key_in.close()  # closes key file.


encrypted_file_path = input("Enter Encrypted file location -> ")  # Encrypted filepath

enc_data = open(encrypted_file_path,'rb')      # Read encrypted file.
encrypted_data = enc_data.read()               # Encrypted data store in encrypted_data variable.

decrypted_files = key.decrypt(encrypted_data)  # Deacryption of data.

new_name = encrypted_file_path[:-10]           # Removing ".encrypted" extension from encrypted file.

out_data = open(new_name + ".decrypted", 'wb') # outputs decrypted file with ".decrypted" extension.
out_data.write(decrypted_files)
