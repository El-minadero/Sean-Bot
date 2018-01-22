'''
Created on Jan 21, 2018

@author: kevinmendoza
'''
import time
import threading
import sys
from root.exchanges.exchangemap import ExchangeMap


time_interval = 5 #in seconds
controller = None

class InputThread(threading.Thread):

    def __init__(self, *args,controller=controller,run_interval=5, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller
        self.run_interval = run_interval
        self._up = False
        self._stop_event = threading.Event()
        
    def run(self):
        print("SEAN BOT ACTIVATED. Will request data every " + str(self.run_interval) +
                  " seconds.\n * BEEP BOOP BEEEEP WEWWT * \n")
        while True:
            if self.controller is not None:
                self.controller.update()
            for x in range(0,self.run_interval):
                time.sleep(1)
                if self._up:
                    self.controller.update()
                    self._up=False
                    break
                
                if self.controller is None:
                    break
                
    def update(self):
        self._up = True
        
    def stop(self):
        self.controller=None
        self._stop_event.set()   
            
class Controller():
    
    def __init__(self):
        print("SEAN BOT controller activated. Attempting to gather config files")
        self.exchanges = self.load_and_connect_exchanges()
        
    def load_and_connect_exchanges(self):
        emap = ExchangeMap(time_delta=time_interval)
        return emap
        pass
    
    def update(self):
        self.exchanges.update()
    
    def save_and_close(self):
        self.exchanges.save_and_close()
    
def print_introduction():
    print("****************************************\n")
    print("Welcome to Sean Bot!\n")
    print("****************************************\n")
    print(""                +       
    "           ,-----.\n"  + 
    "         ,'_/_|_\_`.\n"+
    "        /<<$$8[O]$$>\ \n"+
    "       _|-----------|_\n"+
    "      |  | ====-=- |  |\n"+
    "      |  | -=-==== |  |\n"+
    "      \  | ::::|()||  /\n"+
    "       | | ....|()|| |\n"+
    "       | |_________| |\n"+
    "       | |\_______/| |\n"+
    "      /   \ /   \ /   \ \n"+
    "      `---' `---' `---' \n")
    print("****************************************\n")

def stopping_sean_bot():
    print("****************************************\n")
    print(" * directive acquired. Terminating Sean Bot * \n" )
    time.sleep(0.5)
    print("\n"+
"                         ______\n"+
"                       <((((((\\\ \n"+
"                      /      . }\n"+
"                     ;--..--._|}\n"+
"  (\                 '--/\--'  )\n"+
"   \\\                | '-'  :'|\n"+
"    \\\               . -==- .-|\n"+
"     \\\               \.__.'   \--._\n"+
"     [\\\          __.--|       //  _/'--.\n"+
"     \ \\\       .'-._ ('-----'/ __/      \ \n"+
"      \ \\\     /   __>|      | '--.       |\n"+
"       \ \\\   |   \   |     /    /       /\n"+
"        \ '\ /     \  |     |  _/       /\n"+
"         \  \       \ |     | /        /v\n"+
"          \  \      \        /\n")
    time.sleep(0.5)
    print(" * Hasta La Vista, Bebee... * " )    

def help_code_printout():
    print("here are your possible commands:\n\n"+
          "add new exchange:              new_exchange\n"+
          "modify existing exchange:      modify_exchange\n"+
          "print exchange status:         status\n"+
          "force update:                  update\n"+
          "quit:                          quit\n")
        
def is_help_code(cmd):
    return ("help" in cmd or "?" in cmd)

def is_exit_code(cmd):
    return ("q" in cmd or "quit" in cmd or "exit" in cmd or "stop" in cmd)

def is_update_code(cmd):
    return ("up" in cmd or "update" in cmd)     

def run():
    print_introduction()
    controller      = Controller()
    daemon_thread   = InputThread(controller=controller,daemon=True)
    daemon_thread.start()
    while True:
        cmd = input().lower()
        if is_exit_code(cmd):
            break
        if is_update_code(cmd):
            daemon_thread.update()
        if is_help_code(cmd):
            help_code_printout()
            
    
    stopping_sean_bot()
    controller.save_and_close()
    daemon_thread.stop()
    

if __name__ == '__main__':
    run()