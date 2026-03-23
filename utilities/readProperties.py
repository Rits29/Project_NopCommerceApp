#This file is created to read the properties from the Config.ini file directly. 
#Hence we need to create this file in utility to do so.

import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/Config.ini')

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
