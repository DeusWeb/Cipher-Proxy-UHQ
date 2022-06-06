from colorama import Back, Fore, Style
import os
import requests
import time

banner = (f"""

  /$$$$$$  /$$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$|_  $$_/| $$__  $$| $$  | $$| $$_____/| $$__  $$	- Cipher Proxy Scrapp UHQ !
| $$  \__/  | $$  | $$  \ $$| $$  | $$| $$      | $$  \ $$
| $$        | $$  | $$$$$$$/| $$$$$$$$| $$$$$   | $$$$$$$/	- github.com/deusweb
| $$        | $$  | $$____/ | $$__  $$| $$__/   | $$__  $$
| $$    $$  | $$  | $$      | $$  | $$| $$      | $$  \ $$	- discord.gg/vecna
|  $$$$$$/ /$$$$$$| $$      | $$  | $$| $$$$$$$$| $$  | $$	
 \______/ |______/|__/      |__/  |__/|________/|__/  |__/	
                                                                                               
""")
os.system('cls' if os.name == 'nt' else 'clear')

def main():
	url = f"https://pastebin.com/raw/6fxZssXd"
	r = requests.get(url, allow_redirects=True)
	open('credits.txt', 'wb').write(r.content)
	print(Fore.LIGHTRED_EX + banner)
	print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}~{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Proxy type (http, https, socks4, socks5) :{Fore.RESET}")
	typeproxy = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
	print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}~{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Timeout (default = 1000) :{Fore.RESET}")
	timeout = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
	url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={typeproxy}&timeout={timeout}&country=all&ssl=all&anonymity=all"
	r = requests.get(url, allow_redirects=True)
	open('proxies.txt', 'wb').write(r.content)
	print(f"{Fore.LIGHTGREEN_EX}Succes proxy scrapped! {Fore.RED}\nExiting now...")
	time.sleep(1)
	exit()
main()
