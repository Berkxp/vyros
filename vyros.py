# This tool doens't promove any illegal attitude or pentest with no authorization, this tool its for educacional purposes only
import os
import requests
import random
import time
import sys

os.system('clear')

def banner():
    print('____   ____                           ')
    print('\   \ /   /__.__._______  ____  ______')
    print(' \   Y   <   |  |\_  __ \/  _ \/  ___/')
    print('  \     / \___  | |  | \(  <_> )___ \ ')
    print('   \___/  / ____| |__|   \____/____  >')
    print('          \/                       \/ ')
    print('[*] This tool dont promove web attacks and illegals attitudes')

def banner2():
    print (' ▌ ▐· ▄· ▄▌▄▄▄        .▄▄ · ')
    print('▪️█·█▌▐█▪️██▌▀▄ █·▪️     ▐█ ▀. ')
    print('▐█▐█•▐█▌▐█▪️▐▀▀▄  ▄█▀▄ ▄▀▀▀█▄')
    print(' ███  ▐█▀·.▐█•█▌▐█▌.▐▌▐█▄▪️▐█')
    print('. ▀    ▀ • .▀  ▀ ▀█▄▀▪️ ▀▀▀▀ ')
    print ('[*] This tool dont promove web attacks and illegals attitudes')

def banner3():
    print(' ██▒   █▓▓██   ██▓ ██▀███   ▒█████    ██████ ')
    print('▓██░   █▒ ▒██  ██▒▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ')
    print(' ▓██  █▒░  ▒██ ██░▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ')
    print('  ▒██ █░░  ░ ▐██▓░▒██▀▀█▄  ▒██   ██░  ▒   ██▒')
    print('   ▒▀█░    ░ ██▒▓░░██▓ ▒██▒░ ████▓▒░▒██████▒▒')
    print('   ░ ▐░     ██▒▒▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░')
    print('   ░ ░░   ▓██ ░▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░')
    print('     ░░   ▒ ▒ ░░    ░░   ░ ░ ░ ░ ▒  ░  ░  ░  ')
    print('      ░   ░ ░        ░         ░ ░        ░  ')
    print('     ░    ░ ░                                ')
    print ('[*] This tool dont promove web attacks and illegals attitudes')

def banner4():
    print('██╗   ██╗██╗   ██╗██████╗  ██████╗ ███████╗')
    print('██║   ██║╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝')
    print('██║   ██║ ╚████╔╝ ██████╔╝██║   ██║███████╗')
    print('╚██╗ ██╔╝  ╚██╔╝  ██╔══██╗██║   ██║╚════██║')
    print(' ╚████╔╝    ██║   ██║  ██║╚██████╔╝███████║')
    print('  ╚═══╝     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝')
    print ('[*] This tool dont promove web attacks and illegals attitudes')

def banner5():
    print(' ▄█    █▄  ▄██   ▄      ▄████████  ▄██████▄     ▄████████ ')
    print('███    ███ ███   ██▄   ███    ███ ███    ███   ███    ███ ')
    print('███    ███ ███▄▄▄███   ███    ███ ███    ███   ███    █▀  ')
    print('███    ███ ▀▀▀▀▀▀███  ▄███▄▄▄▄██▀ ███    ███   ███        ')
    print('███    ███ ▄██   ███ ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ')
    print('███    ███ ███   ███ ▀███████████ ███    ███          ███ ')
    print('███    ███ ███   ███   ███    ███ ███    ███    ▄█    ███ ')
    print (' ▀██████▀   ▀█████▀    ███    ███  ▀██████▀   ▄████████▀  ')
    print('                       ███    ███                         ')
    print ('[*] This tool dont promove web attacks and illegals attitudes')
    
def banner6():
    print(' _____ __ __ _____ _____ _____ ')
    print('|  |  |  |  | __  |     |   __|')
    print('|  |  |_   _|    -|  |  |__   |')
    print(' \___/  |_| |__|__|_____|_____|')
    print ('[*] This tool dont promove web attacks and illegals attitudes')
    
def banner7():
    print('     ##### /      ##                                          ')
    print('  ######  /    #####                                          ')
    print(' /#   /  /       #####                                        ')
    print('/    /  ##       / ##                                         ')
    print('    /  ###      /                                             ')
    print('   ##   ##      # ##   ####    ###  /###     /###     /###    ')
    print('   ##   ##      /  ##    ###  / ###/ #### / / ###  / / #### / ')
    print('   ##   ##     /   ##     ###/   ##   ###/ /   ###/ ##  ###/  ')
    print('   ##   ##     #   ##      ##    ##       ##    ## ####       ')
    print('   ##   ##     /   ##      ##    ##       ##    ##   ###      ')
    print('    ##  ##    /    ##      ##    ##       ##    ##     ###    ')
    print('     ## #     #    ##      ##    ##       ##    ##       ###  ')
    print('      ###     /    ##      ##    ##       ##    ##  /###  ##  ')
    print('       ######/      #########    ###       ######  / #### /   ')
    print('         ###          #### ###    ###       ####      ###/    ')
    print('                            ###                               ')
    print('                     #####   ###                              ')
    print('                   /#######  /#                               ')
    print('                  /      ###/                                 ')
    print ('[*] This tool dont promove web attacks and illegals attitudes')
    
def bincheckbanner():
    print('██████╗ ██╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗')
    print('██╔══██╗██║████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝')
    print('██████╔╝██║██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ ')
    print('██╔══██╗██║██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ')
    print('██████╔╝██║██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗')
    print('╚═════╝ ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝')
    print('')
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
    bin_number = input("Type Bin (6 digits): ")
    result = bin_checker(bin_number)

    if result:
        print('')
        print('    🎩 BERKXP')
        print('    💻 VYROS 1.0')
        print('    🏤 BIN CHECKER:')
        print('')
        print("Bin info:")
        print('')
        print(f"🏤 Bank: {result['bank']}")
        print(f"®️ Brand: {result['brand']}")
        print(f"🏷 Type: {result['type']}")
        print(f"🌐 Country: {result['country']}")
        print(f"⬆️ Level: {result['level']}")
    else:
        print("Error.")
        time.sleep(2)
        os.system("clear")
        menuescolha()
        
def tools():
    escolhatool = input('>>> Select a option: ')
    if escolhatool == '1':
        print('[*] Installing Zphisher...')
        os.system('pkg install tur-repo')
        os.system('pkg install zphisher')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('Type "zphisher" to start Zphisher.')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '2':
        print('[*] Installing Txtool...')
        os.system('apt install git')
        os.system('apt install python2')
        os.system('git clone https://github.com/kuburan/txtool.git')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type the follow commands:')
        print('cd ..')
        print('cd txtool')
        print('python install.py')
        print('txtool')
        print('[*] And is done!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(3)
        os.system('clear')
        menuescolha()
    elif escolhatool == '3':
        print('[*] Installing Red Hawk...')
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
        time.sleep(4)
        os.system('clear')
        menuescolha()
    elif escolhatool == '4':
        print('[*] Installing Sql Map...')
        os.system('apt install python')
        os.system('pip install sqlmap')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] Type "sqlmap" to start the tool')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '5':
        print('[*] Installing Black Hydra...')
        os.system('apt install git')
        os.system('git clone https://github.com/Gameye98/Black-Hydra')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] Tool installed sucefully!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(2)
        os.system('clear')
        menuescolha()
    elif escolhatool == '6':
        print('[*] Installing XOIC...')
        os.system('apt install python')
        os.system('pkg install git')
        os.system('git clone https://github.com/StormRLS/XOIC')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type the follow commands:')
        print('cd ..')
        print('cd XOIC')
        print('python XOIC.py')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(4)
        os.system('clear')
        menuescolha()
    elif escolhatool == '7':
        print('[*] Installing Xerxes...')
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
        time.sleep(8)
        os.system('clear')
        menuescolha()
    elif escolhatool == '8':
        os.system('apt install python2')
        os.system('git clone https://github.com/bibortone/D-Tech.git')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] After this type:')
        print('cd ..')
        print('cd D-TECH')
        print('python2 d-tect.py')
        print('')
        print('[*] And is done!')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(5)
        os.system('clear')
        menuescolha()
    elif escolhatool == '9':
        os.system('pkg install nmap')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('[*] just type "nmap" to start the tool.')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        time.sleep(3)
        os.system('clear')
        bannerandom()
    elif escolhatool == '10': hammer()
    elif escolhatool == 'exit':
        os.system('clear')
        exit()
    elif escolhatool == 'help':
        print('')
        print('COMANDS LIST')
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
        print('help   print this help ')
        print('exit   exit tool')
        print('banner  changes banner')
        print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
    elif escolhatool == 'banner':
        os.system('clear')
        bannerandom()
        tools()
    else:
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print('Opção inválida')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■')
        
def main_menu():
    print('')
    print('')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('         MAIN MENU        ')
    print('1 > Bin check')
    print('2 > Ip lookup')
    print('3 > Ddos [OFF]')
    print('4 > Install tools')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■')
     
def ip_lookup(ip_address):
    try:
        # Fazendo a requisição para a API
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        # Convertendo a resposta em JSON
        data = response.json()

        # Exibindo as informações
        print('')
        print(f"Ip info: {ip_address}")
        print('𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃')
        print(f"💻 Hostname: {data.get('hostname', 'N/A')}")
        print(f"🏙 City: {data.get('city', 'N/A')}")
        print(f"🌏 Region: {data.get('region', 'N/A')}")
        print(f"🌍 Country: {data.get('country', 'N/A')}")
        print(f"📍 Location: {data.get('loc', 'N/A')}")
        print(f"🏢 Organization: {data.get('org', 'N/A')}")
        print('𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃')
        print('')
        backmenu3 = input('Back to menu? (yes/no)').lower()
        if backmenu3 == 'yes':
            time.sleep(1)
            os.system('clear')
            menuescolha()
        if backmenu3 == 'no':
            time.sleep(1)
            os.system('clear')
            print('>>> Exiting Vyros...')
            exit()
    except requests.exceptions.RequestException as e:
        print(f"Error while checking ip: {e}")
     
def menuescolha():
    while True:
        bannerandom()
        main_menu()
        escolha = input('>>> Selecione uma opção: ')
        if escolha == '1':
            bininfo()
            time.sleep(2)
            backmenu1 = input('Do you want back to menu? (yes/no) ')
            if backmenu1 == 'yes':
                menuescolha()
            elif backmenu == 'no':
                time.sleep(2)
                print('[*] Exiting Vyros...')
                break
            else:
                print('Invalid Option!')
        elif escolha == '2':
            ip_address = input('Type Ip: ')
            ip_lookup(ip_address)
        elif escolha == '3':
            # implementar ddos
            pass
        elif escolha == '4':
            print('      INSTALL TOOLS')
            print('■■■■■■■■■■■■■■■■■■■■■■')
            print('1 > Zphisher    6 > XOIC')
            print('2 > Txtool.     7 > Xerxes')
            print('3 > Red Hawk.   8 > D-TECH')
            print('4 > Sql Map.    9 > Nmap')
            print('5 > Black-Hydra 10 > Hammer')
            print('■■■■■■■■■■■■■■■■■■■■■■')
            tools()
        elif escolha == 'help':
            print('')
            print('')
            print('COMANDS LIST')
            print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
            print('help   print this help ')
            print('exit   exit tool')
            print('banner  changes banner')
            print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')
            print('')
        elif escolha == 'banner':
            os.system('clear')
            menuescolha()
        elif escolha == 'exit':
            print('[*] Exiting Vyros...')
            exit()
        elif escolha == 'clear':
            os.system('clear')
            menuescolha()

def hammer():
    os.system('git clone https://github.com/cyweb/hammer.git')

menuescolha()
