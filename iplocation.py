"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        creat by Amir Hossein Tadas & TAHA
"""
import os
import sys
import ipapi
from colorama import Fore

def __start__():
    print(Fore.RED+"\n [!] Enter IP Address")
    print(Fore.RED+"\n [/] Or Press The Enter Key :))) \n")
    
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"IP-Location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+">> ")
    source = ipapi.location(ip=site, key=None)
    try:
        print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
        
        print (Fore.GREEN+" [!]"+Fore.BLUE+" ip = "+ source["ip"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" city = " + source["city"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" region = "+ source["region"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" id country = "+source["country"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" country = "+ source["country_name"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Calling Code = "+source["country_calling_code"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Languages = "+source["languages"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" org = "+ source["org"])
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Sorry Please Enter IP Address")

if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()

