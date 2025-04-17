# This tool doens't promove any illegal attitude or pentest with no authorization, this tool its for educacional purposes only
import os
import requests
import random
import time
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init()

os.system('clear')

def banner():
    print(Fore.RED + '    ____   ____                           ')
    print(Fore.RED + '    \   \ /   /__.__._______  ____  ______')
    print(Fore.RED + '     \   Y   <   |  |\_  __ \/  _ \/  ___/')
    print(Fore.RED + '      \     / \___  | |  | \(  <_> )___ \ ')
    print(Fore.RED + '       \___/  / ____| |__|   \____/____  >')
    print(Fore.RED + '              \/                       \/ ')
    print(Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')

def banner2():
    print(Fore.RED + """     ▌ ▐· ▄· ▄▌▄▄▄        .▄▄ · 
    ▪█·█▌▐█▪██▌▀▄ █·▪     ▐█ ▀. 
    ▐█▐█•▐█▌▐█▪▐▀▀▄  ▄█▀▄ ▄▀▀▀█▄
     ███  ▐█▀·.▐█•█▌▐█▌.▐▌▐█▄▪▐█
    . ▀    ▀ • .▀  ▀ ▀█▄▀▪ ▀▀▀▀ """)
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')

def banner3():
    print(Fore.RED + '     ██▒   █▓▓██   ██▓ ██▀███   ▒█████    ██████ ')
    print(Fore.RED + '    ▓██░   █▒ ▒██  ██▒▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ')
    print(Fore.RED + '     ▓██  █▒░  ▒██ ██░▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ')
    print(Fore.RED + '      ▒██ █░░  ░ ▐██▓░▒██▀▀█▄  ▒██   ██░  ▒   ██▒')
    print(Fore.RED + '       ▒▀█░    ░ ██▒▓░░██▓ ▒██▒░ ████▓▒░▒██████▒▒')
    print(Fore.RED + '       ░ ▐░     ██▒▒▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░')
    print(Fore.RED + '       ░ ░░   ▓██ ░▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░')
    print(Fore.RED + '         ░░   ▒ ▒ ░░    ░░   ░ ░ ░ ░ ▒  ░  ░  ░  ')
    print(Fore.RED + '          ░   ░ ░        ░         ░ ░        ░  ')
    print(Fore.RED + '         ░    ░ ░                                ')
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')

def banner4():
    print(Fore.RED + '    ██╗   ██╗██╗   ██╗██████╗  ██████╗ ███████╗')
    print(Fore.RED + '    ██║   ██║╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝')
    print(Fore.RED + '    ██║   ██║ ╚████╔╝ ██████╔╝██║   ██║███████╗')
    print(Fore.RED + '    ╚██╗ ██╔╝  ╚██╔╝  ██╔══██╗██║   ██║╚════██║')
    print(Fore.RED + '     ╚████╔╝    ██║   ██║  ██║╚██████╔╝███████║')
    print(Fore.RED + '      ╚═══╝     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝')
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')

def banner5():
    print(Fore.RED + '     ▄█    █▄  ▄██   ▄      ▄████████  ▄██████▄     ▄████████ ')
    print(Fore.RED + '    ███    ███ ███   ██▄   ███    ███ ███    ███   ███    ███ ')
    print(Fore.RED + '    ███    ███ ███▄▄▄███   ███    ███ ███    ███   ███    █▀  ')
    print(Fore.RED + '    ███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄▄██▀ ███    ███   ███        ')
    print(Fore.RED + '    ███    ███ ▄██   ███ ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ')
    print(Fore.RED + '    ███    ███ ███   ███ ▀███████████ ███    ███          ███ ')
    print(Fore.RED + '    ███    ███ ███   ███   ███    ███ ███    ███    ▄█    ███ ')
    print(Fore.RED + '     ▀██████▀   ▀█████▀    ███    ███  ▀██████▀   ▄████████▀  ')
    print(Fore.RED + '                           ███    ███                         ')
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')
    
def banner6():
    print(Fore.RED + '     _____ __ __ _____ _____ _____ ')
    print(Fore.RED + '    |  |  |  |  | __  |     |   __|')
    print(Fore.RED + '    |  |  |_   _|    -|  |  |__   |')
    print(Fore.RED + '     \___/  |_| |__|__|_____|_____|')
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')
    
def banner7():
    print(Fore.RED + '         ##### /      ##                                          ')
    print(Fore.RED + '      ######  /    #####                                          ')
    print(Fore.RED + '     /#   /  /       #####                                        ')
    print(Fore.RED + '    /    /  ##       / ##                                         ')
    print(Fore.RED + '        /  ###      /                                             ')
    print(Fore.RED + '       ##   ##      # ##   ####    ###  /###     /###     /###    ')
    print(Fore.RED + '       ##   ##      /  ##    ###  / ###/ #### / / ###  / / #### / ')
    print(Fore.RED + '       ##   ##     /   ##     ###/   ##   ###/ /   ###/ ##  ###/  ')
    print(Fore.RED + '       ##   ##     #   ##      ##    ##       ##    ## ####       ')
    print(Fore.RED + '       ##   ##     /   ##      ##    ##       ##    ##   ###      ')
    print(Fore.RED + '        ##  ##    /    ##      ##    ##       ##    ##     ###    ')
    print(Fore.RED + '         ## #     #    ##      ##    ##       ##    ##       ###  ')
    print(Fore.RED + '          ###     /    ##      ##    ##       ##    ##  /###  ##  ')
    print(Fore.RED + '           ######/      #########    ###       ######  / #### /   ')
    print(Fore.RED + '             ###          #### ###    ###       ####      ###/    ')
    print(Fore.RED + '                                ###                               ')
    print(Fore.RED + '                         #####   ###                              ')
    print(Fore.RED + '                       /#######  /#                               ')
    print(Fore.RED + '                      /      ###/                                 ')
    print (Fore.MAGENTA + '[*] This tool does not promote web attacks and illegals attitudes')
    
def bincheckbanner():
    print(Fore.GREEN + """    ██████╗ ██╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔══██╗██║████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    ██████╔╝██║██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ 
    ██╔══██╗██║██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ██████╔╝██║██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
    ╚═════╝ ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝""")
    print(Style.RESET_ALL + '')
    print('')
     
print ('>>> Starting Vyros tool...')

def bannerandom():
        bannerand = random.choice([banner, banner2, banner3, banner4, banner5, banner6, banner7])
        bannerand()

def bin_checker(bin_number):
    url = f"https://lookup.binlist.net/{bin_number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "bank": data.get("bank", {}).get("name"),
            "brand": data.get("brand"),
            "type": data.get("type"),
            "country": data.get("country", {}).get("name"),
            "level": data.get("level"),
        }
    else:
        return None
        
def bininfo():
    os.system("clear")
    bincheckbanner()
    bin_number = input("Type Bin (6/8 digits): ")
    result = bin_checker(bin_number)

    if result:
        print('')
        print(Fore.RED + '    🎩 BERKXP')
        print(Fore.RED + '    💻 VYROS 1.0')
        print(Fore.RED + '    🏤 BIN CHECKER:')
        print('')
        print(Fore.RED + "Bin info:")
        print('')
        print(Fore.RED + f"🏤 Bank: {result['bank']}")
        print(Fore.RED + f"✅️ Level: {result['brand']}")
        print(Fore.RED + f"🏷 Type: {result['type']}")
        print(Fore.RED + f"🌐 Country: {result['country']}")
    else:
        print(Fore.RESET + "Error.")
        time.sleep(2)
        os.system("clear")
        menuescolha()
        
def tools():
    escolhatool = input(Fore.MAGENTA + '>>> Select a option: ')
    if escolhatool == '1':
        print(Fore.CYAN + '[*] Installing Zphisher...')
        os.system('pkg install tur-repo')
        os.system('pkg install zphisher')
        print(Fore.RED + '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('Type "zphisher" to start Zphisher.')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '2':
        print(Fore.CYAN + '[*] Installing Txtool...')
        os.system('apt install git')
        os.system('apt install python2')
        os.system('git clone https://github.com/kuburan/txtool.git ')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type the follow commands:')
        print('cd ..')
        print('cd txtool')
        print('python install.py')
        print('txtool')
        print('[*] And is done!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(3)
        os.system('clear')
        menuescolha()
    elif escolhatool == '3':
        print(Fore.CYAN+ '[*] Installing Red Hawk...')
        os.system('apt install git')
        os.system('apt install php')
        os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] Tool instaled sucefully!')
        print('[*] Type the follow commands to start the tool:')
        print('>>> cd ..')
        print('>>> cd RED_HAWK')
        print('>>> php rhawk.php')
        print('[*]And is done!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(4)
        os.system('clear')
        menuescolha()
    elif escolhatool == '4':
        print(Fore.YELLOW + '[*] Installing Sql Map...')
        os.system('apt install python')
        os.system('pip install sqlmap')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] Type "sqlmap" to start the tool')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '5':
        print(Fore.RED + '[*] Installing Black Hydra...')
        os.system('apt install git')
        os.system('git clone https://github.com/Gameye98/Black-Hydra')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] Tool installed sucefully!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '6':
        print(Fore.MAGENTA + '[*] Installing XOIC...')
        os.system('apt install python')
        os.system('pkg install git')
        os.system('git clone https://github.com/StormRLS/XOIC')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type the follow commands:')
        print('cd ..')
        print('cd XOIC')
        print('python XOIC.py')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(4)
        os.system('clear')
        menuescolha()
    elif escolhatool == '7':
        print(Fore.RED + '[*] Installing Xerxes...')
        os.system('pkg install git -y && git clone https://github.com/XCHADXFAQ77X/XERXES')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this is just type:')
        print('cd ..')
        print('cd XERXES')
        print('gcc -o xerxes xerxes.c')
        print('./xerxes (ip) (port)')
        print('Example:')
        print('./xerxes 192.168.1.8 443')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(8)
        os.system('clear')
        menuescolha()
    elif escolhatool == '8':
        os.system('apt install python2')
        os.system('git clone https://github.com/bibortone/D-Tech.git')
        print(Fore.BLUE + '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type:')
        print('cd ..')
        print('cd D-TECH')
        print('python2 d-tect.py')
        print('')
        print('[*] And is done!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(5)
        os.system('clear')
        menuescolha()
    elif escolhatool == '9':
        os.system('pkg install nmap')
        print(Fore.CYAN + '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] just type "nmap" to start the tool.')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        time.sleep(3)
        os.system('clear')
        bannerandom()
    elif escolhatool == '10': hammer()
    elif escolhatool == 'exit':
        os.system('clear')
        exit()
    elif escolhatool == 'help':
        print(Fore.RED + '')
        print('COMANDS LIST')
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
        print('help   print this help ')
        print('exit   exit tool')
        print('banner  changes banner')
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
        print(Fore.RESET + '')
    elif escolhatool == 'banner':
        os.system('clear')
        bannerandom()
        tools()
    else:
        print(Fore.CYAN + '■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('Opção inválida')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(Fore.RESET + '')
        
def main_menu():
    print(Fore.RESET + '')
    print('')
    print(Fore.CYAN + '■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('         MAIN MENU        ')
    print('1 > Bin check')
    print('2 > Ip lookup')
    print('3 > Ddos [OFF]')
    print('4 > Install tools')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■')
    print(Fore.RESET + '')
     
def ip_lookup(ip_address):
    try:
        # Fazendo a requisição para a API
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        # Convertendo a resposta em JSON
        data = response.json()

        # Exibindo as informações
        print('')
        print(Fore.RED + f"Ip info: {ip_address}")
        print('𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃')
        print(f"💻 Hostname: {data.get('hostname', 'N/A')}")
        print(f"🏙 City: {data.get('city', 'N/A')}")
        print(f"🌏 Region: {data.get('region', 'N/A')}")
        print(f"🌍 Country: {data.get('country', 'N/A')}")
        print(f"📍 Location: {data.get('loc', 'N/A')}")
        print(f"🏢 Organization: {data.get('org', 'N/A')}")
        print('𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃')
        print(Fore.RESET + '')
        backmenu3 = input(Fore.CYAN + 'Back to menu? (yes/no)').lower()
        print(Fore.RESET + '')
        if backmenu3 == 'yes':
            time.sleep(1)
            os.system('clear')
            menuescolha()
        if backmenu3 == 'no':
            time.sleep(1)
            os.system('clear')
            print(Fore.CYAN + '>>> Exiting Vyros...')
            print(Fore.RESET + '')
            exit()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error while checking ip: {e}")
     
def menuescolha():
    while True:
        bannerandom()
        main_menu()
        escolha = input(Fore.CYAN + '>>> Option: ')
        if escolha == '1':
            bininfo()
            time.sleep(2)
            backmenu1 = input(Fore.CYAN + 'Do you want back to menu? (yes/no) ')
            if backmenu1 == 'yes':
                menuescolha()
            elif backmenu1 == 'no':
                time.sleep(2)
                print(Fore.RESET + '[*] Exiting Vyros...')
                exit()
            else:
                print('Invalid Option!')
        elif escolha == '2':
            ip_address = input(Fore.CYAN + 'Type Ip: ')
            ip_lookup(ip_address)
        elif escolha == '3':
            # implementar ddos
            pass
        elif escolha == '4':
            print(Fore.CYAN + '      INSTALL TOOLS')
            print('■■■■■■■■■■■■■■■■■■■■■■')
            print('1 > Zphisher    6 > XOIC')
            print('2 > Txtool.     7 > Xerxes')
            print('3 > Red Hawk.   8 > D-TECH')
            print('4 > Sql Map.    9 > Nmap')
            print('5 > Black-Hydra 10 > Hammer')
            print('■■■■■■■■■■■■■■■■■■■■■■')
            print(Fore.RESET + '')
            tools()
        elif escolha == 'help':
            print(Fore.RESET + '')
            print('')
            print(Fore.CYAN + '    COMANDS LIST')
            print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
            print('help   print this help ')
            print('exit   exit tool')
            print('banner  changes banner')
            print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
            print(Fore.RESET + '')
        elif escolha == 'banner':
            os.system('clear')
            menuescolha()
        elif escolha == 'exit':
            print(Fore.RESET + '[*] Exiting Vyros...')
            exit()
        elif escolha == 'clear':
            os.system('clear')
            menuescolha()

def hammer():
    os.system('git clone https://github.com/cyweb/hammer.git')

menuescolha()
