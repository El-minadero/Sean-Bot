'''
Created on Jan 6, 2018

@author: kevinmendoza
'''

import numpy as np

def make_index_dict(data=None):
    indices = {}
    indices[RSI.name] = RSI(data)
    return indices


class Index():
    '''
        basic index class used to calculate something important
    '''
    name = "default"
    def __init__(self,data=None,**kwargs):
        self.data = data
        self._index = 0.0
        
    def update(self):
        pass
    
    
class RSI(Index):
    name = "Relative Strength Index"
    def __init__(self,period="14:00:00:00",divisions="00:06:00:00",**kwargs):
        super().__init(**kwargs)
        self.period     = period
        self.divisions  = divisions
        
    def update(self):
        timeseries      = self.data.get_timeseries(self.period,self.divisions)
        up_periods      = self.__get_up_periods(timeseries)
        down_periods    = self.__get_down_periods(timeseries)
        rs = np.divide(up_periods,down_periods)
        
        self._index = 100 - 100*np.divide(1,1+rs)
        
    def __get_up_periods(self,timeseries):
        market_price= timeseries["market_price"]
        dv          = np.diff(market_price)
        indices     = np.where(dv>0.0)
        market_price_pos = market_price[indices]
        return np.average(market_price_pos)
        
    def __get_down_periods(self,timeseries):
        market_price= timeseries["market_price"]
        dv          = np.diff(market_price)
        indices     = np.where(dv<0.0)
        market_price_neg = market_price[indices]
        return np.average(market_price_neg)
        