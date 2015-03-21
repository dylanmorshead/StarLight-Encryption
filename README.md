# StarLight-Encryption

StarLight Encryption a simple to use, but secure command line file encryption utility.

To do, clean up comments, make it more understandable.

Find and fix bugs and add more plugins and features.

StarLight Encryption usage


-f filename defines a filename

-e yes -e encrypts, argument yes to encrypt

-d yes -d decrypts, argument yes to decrypt

-p password, classical password

-cipher AES, choose a cipher from the plugins, to write a plugin(optional unless you want to use other plugins) default AES

if your still confused, here is a understandable example, for both encryption and decryption

-e yes -f secretimage.png -p asupersecretpassword -cipher AES

-d yes -f secretimage.png.aes -p asupersecretpassword -cipher AES

for an example on how to write a plugin, check example.py

-show w - shows GNU licence

requirements

pycrypto

pygame(mostly for mouse input and secure hash generation)

