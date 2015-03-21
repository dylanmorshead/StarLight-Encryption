import os, random, struct
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
import progressbar
#This is the AES plugin, its the main plugin.

#this function checks to see if the module can be used, 
#all plugins must follow the same layout

#you can use this as an example, you have do cut the IV here into how many
# bits / bytes is needed

salt = "AESH89A1"

def __init__():
    return True 
	
#this function encrypts

def encrypt(filename, password, iv):
    chucksize=64*1024
    out_filename = filename + ".aes"
    iv = iv[:16]

    secure_key = KDF.PBKDF1(password, salt, 16, count = 1000)

    encryptor = AES.new(secure_key, AES.MODE_CBC, iv)

    filesize = os.path.getsize(filename)
    progress = progressbar.AnimatedProgressBar(end=filesize, width=50)

    with open(filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chucksize)
                if len(chunk) == 0:
                    # we are finished
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                    

                    # show the progress bar
                
                
                outfile.write(encryptor.encrypt(chunk))
                progress + len(chunk)
                progress.show_progress()
            print ""
            print "Done!"
    
	
#this function decrypts

def decrypt(filename, password):
    chucksize=64*1024
    secure_key = KDF.PBKDF1(password, salt, 16, count = 1000)
    out_filename = os.path.splitext(filename)[0]

    with open(filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(secure_key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(filename)
        progress = progressbar.AnimatedProgressBar(end=filesize, width=50)
        
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chucksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
                progress + len(chunk)
                progress.show_progress()

            outfile.truncate(origsize)
        print ""
        print "Done!"
