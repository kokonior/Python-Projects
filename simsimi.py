import requests
from colorama import init, Fore

init(autoreset=True)

def autochat(message):
    
    req = requests.get(f'https://dkmpostor-auto-chat.herokuapp.com/autochat?message={message}&lang=id')
    res = req.json()
    
    if res['statusCode'] == 200:
        return res['message_info']['message_reply']
    
def main():
    
    while True:
        message = input(Fore.GREEN + 'You : ')
        print(Fore.BLUE + 'Bot : ' + autochat(message))
    
    
if __name__ == '__main__':

    print('''
   _____ _           _   _           _   
  / ____| |         | | | |         | |  
 | |    | |__   __ _| |_| |__   ___ | |_ 
 | |    | '_ \ / _` | __| '_ \ / _ \| __|
 | |____| | | | (_| | |_| |_) | (_) | |_ 
  \_____|_| |_|\__,_|\__|_.__/ \___/ \__|
                                             
    ''')
    
    main()