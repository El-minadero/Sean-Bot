'''
Created on Jan 3, 2018

@author: kevinmendoza
'''

class Messager():
    
    def __init__(self,**kwargs):
        pass
    
    def message(self,message=None):
        pass
            

class TelegramWrapper(Messager):
    '''
            this class wraps the Telegram API and ensures a quick, easy way
        to message users. Each object instance is associated with a 
        corresponding phone number. Messages are sent via the message command
    '''

    def __init__(self,address=None,**kwargs):
        super().__init__()
        self.address=address
        
    '''
        send a message to the address. If no message is provided will send
        default 'None' message
    '''
    def message(self,message=None):
        if message is None:
            self._test_message_()
        else:
            pass
        
    '''
        send a test message to the address
    '''
    def _test_message_(self):
        pass
        
        
        
        