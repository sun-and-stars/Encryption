from cryptography.fernet import Fernet
import os.path

# this code makes a new Key for Symmetric encryption.
new_key = Fernet.generate_key()


# Taking file parameters.
name_of_file = input("Enter a name for key out file with txt extension -> ") # This line takes input for file name.
path_for_file = input("Enter the path of where to store key file -> ") # This line takes input to where store the file.
complete_name = os.path.join(path_for_file, name_of_file) # This line joins path and file name.



#print(new_key)
key_out = open(complete_name,'wb')        # This line opens a file in write byte mode.
key_out.write(new_key)          # This line prints out the key to an external text file.
file_close = key_out.close()
