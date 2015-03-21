import os
import sys

# StarLight Encryption plugin loader

__author__ = "Dylan Morshead"
__copyright__ = "Copyright 2015, Dylan Morshead"
__credits__ = ["Dylan Morshead"] #add names here if desired
__licence__  = "GPL"
__version__ = "0.01"
__email__ = "dylanmorshead@gmail.com"
__status__ = "Development"

plugins = []

loaded_plugins = []

# this gets all the plugins in the ./plugins folder

def get_plugins():
    #for filename in os.listdir('plugins'):
    for filename in os.listdir(os.path.dirname(__file__) + './plugins'):

        # remove file extension
        
        filename = filename.replace(".pyc", "")
        filename = filename.replace(".py", "")
        
        plugins.append(filename)
    return plugins

# this loads the plugins  
        
def load_plugins():
    # we get the list of plugins
    plugins = get_plugins()
    #sys.path.insert(0, './plugins')
    #sys.path.insert(0, './plugins')
    sys.path.insert(0, os.path.dirname(__file__) + './plugins')
    for plugin in plugins:

        # import plugins
        
        mod = __import__("%s" %  plugin)

        # we are going to check if the plugin contains the main entry call
        # then we will display weather or not its a vaild call :D we will still load
        # the plugin however, but inform the user its not a vaild plugin

        if mod.__init__() == True:
            print "%s is a valid StarLight Encryption plugin" % plugin
        else:
            print "%s is not a vaild StarLight Encryption plugin" % plugin
            
        loaded_plugins.append(mod)

    return loaded_plugins

# this calls the plugin based on the plugin name

def call_plugin(plugin, filename, password, iv , options):
    if options == "encrypt":
        loaded_plugins[plugins.index(plugin)].encrypt(filename, password, iv)
    if options == "decrypt":
        loaded_plugins[plugins.index(plugin)].decrypt(filename, password)

