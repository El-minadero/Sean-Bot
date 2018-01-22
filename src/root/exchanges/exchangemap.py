'''
Created on Jan 21, 2018

@author: kevinmendoza
'''
import os.path
import time
from root.exchanges import exchange
exchange_settings_filepath=""
approved_exchanges = {}

def fill_approved_exchanges():
    approved_exchanges = exchange.fill_exchanges()

def print_file_exists():
    print("exchange settings file " + str(exchange_settings_filepath) + " exists")
    
def print_file_failure():
    time.sleep(0.25)
    print("exchange settings file " + str(exchange_settings_filepath) + " can not be found!!!")
    time.sleep(0.25)
    print("consider providing your own path via the \'path=*mypath*\' command")

def valid_exchange(key):
    return print("valid exchange protocol discovered for \'" + str(key) + "\'\n adding it to map...")

class ExchangeMap():
    time_delta = 1
    def __init__(self,time_delta=1,**kwargs):
        self.time_delta = time_delta
        self.exchanges = {}
        self.exchange_name_list = []
        self._connect_settings()
        self._load_settings()
        
    def _connect_settings(self):
        self.success = os.path.exists(exchange_settings_filepath)
        if self.success:
            print_file_exists()
            fill_approved_exchanges()
            with open(exchange_settings_filepath) as fp:
                self._set_exchange_list(fp)
            self.success = len(self.exchange_name_list)>0
        else:
            print_file_failure()

    def _set_exchange_list(self,fp):
        line = fp.readline()
        while line:
            for key in approved_exchanges.keys():
                if key in line.lowercase():
                    self.exchange_name_list.append(key)
                    break

    def _load_settings(self):
        if self.success:
            for exchange in self.exchange_name_list:
                valid_exchange(exchange)
                self.exchanges[exchange] = approved_exchanges[exchange].set_base_path(exchange_settings_filepath)
                self.exchanges[exchange].connect()
                
    def update(self):
        if len(self.exchanges)==0:
            print("NO EXCHANGES PRESENT!!! Unable to update. \n"+
              "* Reminder, Sean Bot is useless without love :( *")
        for exchange in self.exchanges:
            exchange.update()
    
    def save_and_close(self):
        if len(self.exchanges)==0:
            print("NO EXCHANGES PRESENT!!! Unable to save anything to file!\n"+
                  "* Reminder, Sean Bot is useless without love :( *")
        for exchange in self.exchanges:
            exchange.save_and_close()
