import os, random, struct
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
#This is a EXAMPLE plugin


salt = "AESH89A1" # we can use random salts, but don't change it at all once it
# is released

def __init__():
    return True  # vaild plugins must return true
	
#this function encrypts

def encrypt(filename, password, iv):
    print "Encrypt"    
	
#this function decrypts

def decrypt(filename, password):
    print "Decrypt"
