import requests, re, os
from colorama import *

def main():
    m = f'{Fore.MAGENTA}'
    os.system('cls; clear')
    print(f'{m}Welcome to the SkidSearch API!\n')
    s = input(f'{m}What do you wanna lookup:{Fore.CYAN} ')
    method = input(f'{m}What method (username/uuid):{Fore.CYAN} ')
    try:
        if method == 'username':
            r = requests.post(
                url='https://skidsearch.net/panel/index.php', 
                data={"query": s, "method": "username"}, 
                cookies={"PHPSESSID": "PHPSESSID", "__cfduid": "__cfduid", "cf_clearance": "cf_clearance"},
                headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            )
            lol = re.findall(r'(\<p><br>Database:+(.*))', r.text)[0][1]
            s = lol.replace('<br>', ' ')
            k = s.replace('</div>', ' ')
            l = k.replace('</p>', '')  
            lmao = l.replace(' __________________________________________<p>', '\n')
            kek = lmao.replace('Database: ', '')
            uuid = kek.replace('UUID', f'{Fore.WHITE}UUID{Fore.CYAN}')
            username = uuid.replace('Username', f'{Fore.WHITE}Username{Fore.CYAN}')
            final = username.replace('IP:', f'{Fore.WHITE}IP{Fore.CYAN}')
            print(f'{Fore.WHITE}{Fore.CYAN}' + final)
        
        if method == 'uuid':
            r = requests.post(
                url='https://skidsearch.net/panel/index.php', 
                data={"query": s, "method": "uuid"}, 
                cookies={"PHPSESSID": "PHPSESSID", "__cfduid": "__cfduid", "cf_clearance": "cf_clearance"},
                headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            )
            lol = re.findall(r'(\<p><br>Database:+(.*))', r.text)[0][1]
            s = lol.replace('<br>', ' ')
            k = s.replace('</div>', ' ')
            l = k.replace('</p>', ' ')  
            lmao = l.replace(' __________________________________________<p>', '\n')
            kek = lmao.replace('Database: ', '')
            uuid = kek.replace('UUID', f'{Fore.WHITE}UUID{Fore.CYAN}')
            username = uuid.replace('Username', f'{Fore.WHITE}Username{Fore.CYAN}')
            final = username.replace('IP:', f'{Fore.WHITE}IP{Fore.CYAN}')
            print(f'{Fore.WHITE}\n{Fore.CYAN}' + final)
    except:
            print(f'{Fore.RED}Enountered error, please change cookies!')
main()
