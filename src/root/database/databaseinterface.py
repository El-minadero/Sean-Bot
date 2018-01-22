'''
Created on Jan 3, 2018

@author: kevinmendoza
'''

class DatabaseWrapper():
    '''
        creates a new database or connects to an existing one
    '''

    def __init__(self, **kwargs):
        '''
            ? constructor
        '''
        
    def save_data(self,index_id=0,data={},**kwargs):
        pass #??
    
    '''
        returns a timeseries based on stored data and time parameters
        @param period
            Optional. Defaults to 1 hr. Specify the period of interest 
            extending from the most recent collected data back in time 
            via the "dd:HH:MM:SS" timestring. 
        @param divisions.
            Optional. Defaults to 1 minute. Specify the time divisions
            requested in the returned data. 
        @returns
            returns a dict object consisting of the following keys:
            time:   
                    a 1-d numpy array consisting of time (in seconds) 
                    corresponding from the first time in the sequence to 
                    the current time in the sequence.
            market_price: 
                    a 1-d numpy array consisting of the average market 
                    price in each time bin.
            volume: a 1-d numpy array consisting of the total volume of 
                    trades in each time bin.
    ''' 
    def get_timeseries(self,period="00:01:00:00",divisions="00:00:00:00"):
        return None
    
    