'''
Created on Jan 3, 2018

@author: kevinmendoza
'''
from root.exchanges.index import make_index_dict

class Exchange():
    '''
        A class to fetch data from exchanges and automatically calculate
        relevant indices 
        @param data    
            a Data() object from which time series data of market price, order book information, and volume is obtainable
        @param notices
            a dict of Notice() objects
    '''
    def __init__(self,data=None,notices={},**kwargs):
        self._notices   = notices
        self._data      = data
        self.indices    = make_index_dict(data=data)
    
    '''
        updates the data and indices in the exchange
    '''
    def update(self):
        self._data.update()
        self._update_indexes()
        
    '''
        return notices flagged by the notice conditions
    '''
    def get_notices(self):
        self._update_notices()
        notices = {}
        for notice in self._notices:
            if notice.notify():
                notices[notice.name] = notice.get_notice()
        return notices
    
    def _update_notices(self):
        for notice in self._notices:
            notice.update_notice(self.indices)
        
    def _update_indexes(self):
        for index in self._indices:
            index.update()

