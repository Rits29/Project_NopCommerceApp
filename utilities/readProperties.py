#This file is created to read the properties from the Config.ini file directly. 
#Hence we need to create this file in utility to do so.

import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/Config.ini')

# This class is used to read the configuration properties from the Config.ini file.
# It contains static methods to get the base URL, username, and password for each data given in the Config.ini file,
#   we need to create separate methods (static) for each property we want to read.
# Static methods are used here because we do not need to create an instance of this class to access its methods.
# This allows us to call these methods directly using the class name without needing to instantiate it, 
#    i.e., adding an object of the class hence no need to use self parameter.

class ReadConfig():

    @staticmethod
    def getBaseUrl():
        url = config.get(section='common info', option='base_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password