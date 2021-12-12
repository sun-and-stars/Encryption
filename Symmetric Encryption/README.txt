Following scripts are not tested thoroughly and are written just because I had some time on hand.

Following python3 scripts use cryptogrpahy module.
To use them mdoule needs to be installed on the system.
If you do not have module installed, you can check the following link. (https://pypi.org/project/cryptography/)

The Encrypted files will always end with ".encrypted" exension.
While 
The Decrypted files will always end with ".decrypted" extension.

On windows machine you might not need to restore the original file exetension, for files to work again.

Fernet module is used in these scripts to handle Key generation, File encryption and decryption.
To learn more about the module you can check this link. (https://cryptography.io/en/latest/fernet/).

Following scripts are ideal to use on small files, but might now work with large as the file should be available in the memory.
If the files are larger than the memory size the Scripts might not work.

I hope these scripts are useful to you.
