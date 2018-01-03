'''
Created on Jan 3, 2018

@author: kevinmendoza
'''

class ExchangeInterface():
    
    def __init__(self,**kwargs):
        pass
    
    def getInfo(self):
        pass


class Exchange(ExchangeInterface):
    '''
        A class to read data from external exchanges
    '''

    def __init__(self,**kwargs):
        '''
        creates an exchange interaction wrapper object
        '''
        super().__init__(**kwargs)
        
    '''
        returns a dict object of up to date information from the exchange
    '''
    def getInfo(self):
        return {}
    
    
    