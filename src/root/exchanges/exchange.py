'''
Created on Jan 3, 2018

@author: kevinmendoza
'''

def fill_exchanges():
    exchange_dict = {}
    exchange_dict["Binance"]=Binance() 
    return exchange_dict
    
class Exchange():
    '''
        A class to fetch data from exchanges and automatically calculate
        relevant indices 
        @param data    
            a Data() object from which time series data of market price, order book information, and volume is obtainable
        @param notices
            a dict of Notice() objects
    '''
    def __init_(self):
        self.name = "dummy exchange"
        self.path = ""
        
    def update(self):
        print("Updating " + self.name)
        pass
    
    def set_base_path(self,path):
        self.path = path + self.extension
        print("Setting \'" + self.name + "\' path to \'" + self.path + "\'")
    
    def save_and_close(self):
        print("Saving " + self.name + " to file")
        
    def connect(self):
        print("connecting " + self.name + " data")

class Binance(Exchange):
    def __init__(self):
        self.name       = '## binance exchange ##'
        self.extension  = "\binance"
        self.path       = ""
    
    def update(self):
        super().update()
    
    def save_and_close(self):
        print("saving" + str(self.name) + "data to file")
    
    def set_base_path(self,path):
        super().set_base_path(self.extension,path)
        return self
    
    def connect(self):
        super().connect()