# This tool doens't promove any illegal attitude or pentest with no authorization, this tool its for educacional purposes only
import os
import requests
import random
import webbrowser
import time
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
     
print ('>>> Starting Vyros tool...')
banner5()

def bannerandom():
        bannerand = random.choice([banner, banner2, banner3, banner4, banner5, banner6, banner7])
        bannerand()
        
def binchecker1():
     bin = input('Type bin: ')
     result = bin_check(bin)

def bin_check(bin):
    api_url = (f"https://api.binlist.net/v1/details/{bin}")
    response = requests.get(api_url)
    if response.status_code == '200':
        data = response.json()
        return {
            "bin": bin,
            "type": data["type"],
            "brand": data["brand"],
            "country": data["country"]["name"],
            "bank": data["bank"]["name"]
        }
    else:
        return None
        
def imprime_informacoes_bin(result):
    if result:
        print(f"Bin: {result['bin']}")
        print(f"Tipo: {result['type']}")
        print(f"Marca: {result['brand']}")
        print(f"País: {result['country']}")
        print(f"Banco: {result['bank']}")
        print('Bin Checked!')
    else:
        print('Erro ao verificar bin')
 
def tools():
    escolhatool = input('>>> Select a option: ')
    if escolhatool == '1':
        print('[*] Installing Zphisher...')
        os.system('pkg install tur-repo')
        os.system('pkg install zphisher')
        print('Type "zphisher" to start Zphisher.')
    elif escolhatool == '2':
        print('[*] Installing Txtool...')
        os.system('apt install git')
        os.system('apt install python2')
        os.system('git clone https://github.com/kuburan/txtool.git /data/data/com.termux/files/home/')
        print('[*] After this type the follow commands:')
        print('cd')
        print('cd txtool')
        print('python install.py')
        print('txtool')
        print('[*] And is done!')
    elif escolhatool == '3':
        print('[*] Installing Red Hawk...')
        os.system('apt install git')
        os.system('apt install php')
        os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK /data/data/com.termux/files/home/')
        print('[*] Tool instaled sucefully!')
        print('[*] Type the follow commands to start the tool:')
        print('>>> cd')
        print('>>> cd RED_HAWK')
        print('>>> php rhawk.php')
        print('[*]And is done!')
    elif escolhatool == '4':
        print('[*] Installing Sql Map...')
        os.system('apt install python')
        os.system('pip install sqlmap')
        print('[*] Type "sqlmap" to start the tool')
    elif escolhatool == '5':
        print('[*] Installing Black Hydra...')
        os.system('apt install git')
        os.system('git clone https://github.com/Gameye98/Black-Hydra /data/data/com.termux/files/home/')
        print('[*] Tool installed sucefully!')
    elif escolhatool == 'exit':
        os.system('clear')
        exit
    elif escolhatool == 'help':
        print('list cmds')
        print('help   print this help screen')
        print('exit   exit tool')
        print('banner   change banner')
    elif escolhatool == 'banner':
        bannerandom()
        tools()
    else:
        print('Opção inválida')
        
def main_menu():
    print('')
    print('')
    print('########################')
    print('       MAIN MENU        ')
    print('1 > Bin check')
    print('2 > Ip lookup')
    print('3 > Ddos')
    print('4 > Install tools')
    print('########################')

def ip_lookup():
    escolhaip = input('Type IP: ')
    print('[*] Redirecting...')
    time.sleep(3)
    webbrowser.open(f'https://whatismyipaddress.com/ip/{escolhaip}')
    time.sleep(2)
    backmenu = input('Do you want back to menu? (yes/no) ')
    if backmenu == 'yes':
        menuescolha()
    elif backmenu == 'no':
        pyautogui.hotkey('crtl', 'c')
        pytautogui.press('enter')
    else:
        print('Invalid Option!')    
def menuescolha():
    while True:
        main_menu()
        escolha = input('>>> Selecione uma opção: ')
        if escolha == '1':
            binchecker1()
            time.sleep(2)
            backmenu1 = input('Do you want back to menu? (yes/no) ')
            if backmenu1 == 'yes':
                menuescolha()
            elif backmenu == 'no':
                time.sleep(2)
                pyautogui.hotkey('crtl', 'c')
                pytautogui.press('enter')
            else:
                print('Invalid Option!')
        elif escolha == '2':
            ip_lookup()
        elif escolha == '3':
            # implementar ddos
            pass
        elif escolha == '4':
            print('             INSTALL TOOLS')
            print('1 > Zphisher')
            print('2 > Txtool')
            print('3 > Red Hawk')
            print('4 > Sql Map')
            print('5 > Black-Hydra')
            tools()
        elif escolha == 'help':
            print('')
            print('')
            print('list cmds')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('help   print this help screen')
            print('exit   exit tool')
            print('banner   change banner')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('')
        elif escolha == 'banner':
            bannerandom()
        elif escolha == 'exit':
            print('[*] Exiting Vyros...')
            break
        elif escolha == 'clear':
            os.system('clear')
            print(bannerandom)
            menuescolha()

menuescolha()