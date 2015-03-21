#!/usr/bin/env python

import os
import sys
import loader # this is our plugin loader
import pygame
import hashlib
import optparse

__author__ = "Dylan Morshead"
__copyright__ = "(c) 2015 Dylan Morshead"
__credits__ = ["Dylan Morshead"] #add names here if desired
__licence__  = "GPL"
__version__ = "0.01"
__email__ = "dylanmorshead@gmail.com"
__status__ = "Development"

# Starlight Encryption is a simple to use file encryption software,
# that allows plugins and is fully free and open source, written
# completely from scratch, this part of the code is the "backend",
# as we are still working on a front end, the plugin folder is /plugins,
# to write plugins, look at /plugins/how-to.txt, which we will eventully write.

def display_copyright():
    print ""
    print "StarLight Encryption " + "[Version " + __version__ + "]"
    print __copyright__
    print "This program comes with ABSOLUTELY NO WARRANTY; for details type `--show w'."
    print "This is free software, and you are welcome to redistribute it"
    print "under certain conditions; type `--show w' for details."
    print ""

def display_gpl():
    print ""
    with open(os.path.dirname(__file__) + '/gpl.txt') as gpl:
        for line in gpl:
            print line,
    print ""

def main():

    display_copyright()
    
    p = optparse.OptionParser()
    p.add_option('--filename', '-f', default=None)
    p.add_option('--encrypt', '-e', default = None)
    p.add_option('--decrypt', '-d', default = None)
    p.add_option('--password', '-p', default=None)
    p.add_option('--cipher', '-c', default="AES")
    p.add_option('--show', '-s', default="AES")
    options, arguments = p.parse_args()

    if options.show == 'w':
        display_gpl()
        
    
    if options.filename == None:
        print "Please enter a filename"
    if options.encrypt == None and options.decrypt == None:
        print "Please enter encrypt or decrypt"
    if options.password == None:
        print "Please enter a password"
    else:
        if options.encrypt == "yes":
            # we have to load the plugins
            try:
                loader.load_plugins()
            except Exception as e:
                print "error:", e
            #we need to generate a secure IV so we do so here
            x = y = 0
            pygame.init()
            screen = pygame.display.set_mode((640, 100))
            pool_data = []
            WHITE = (255,255,255)
            clock = pygame.time.Clock()
            pygame.display.set_caption('Secure IV Generator')
            basicfont = pygame.font.SysFont(None, 48)
            displayfont = pygame.font.SysFont(None, 20)
            while True:
                event = pygame.event.poll()
                pygame.display.flip() 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.MOUSEMOTION:
                    pool_data.append((event.pos)[0] + (event.pos)[1]) 
                    text = basicfont.render(str(hashlib.md5(str((event.pos)[0] + (event.pos)[1])).hexdigest()), 1, (0,0,0))
                    screen.fill(WHITE)
                    screen.blit(text, (5,50))
        
                information = basicfont.render("Move mouse to generate secure hash", 1, (0,0,0))
                screen.blit(information, (5,10))

            iv = hashlib.md5(str(pool_data)).hexdigest()
            try:
                loader.call_plugin(options.cipher, options.filename, options.password, iv, "encrypt")
            except Exception as e:
                print "error:", e
                        
        if options.decrypt == "yes":
            # this encrypts the file :D
            try:
                loader.load_plugins()
            except Exception as e:
                print "error:", e
            try:
                loader.call_plugin(options.cipher, options.filename, options.password, None, "decrypt")
            except Exception as e:
                print "error:", e
    
    
if __name__ == '__main__': main()

