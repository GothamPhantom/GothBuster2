
# Author : GothamPhantom

import requests
from tqdm import tqdm
import termcolor

print(""" \x1b[38;5;214m
 ██████╗  ██████╗ ████████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔════╝ ██╔═══██╗╚══██╔══╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██║  ███╗██║   ██║   ██║   ███████║███████║██╔████╔██║██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██║   ██║██║   ██║   ██║   ██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
╚██████╔╝╚██████╔╝   ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
		""")
target_url = input('[+GothBuster+] URL: ')
file_name = input('[+GothBuster+] Wordlist path: ')

print(""" \x1b[38;5;214m
===============================================================
GothBuster v2.0
by GothamPhantom
===============================================================
[*] Url:                    """, target_url, """
[*] Method:                  GET
[*] Wordlist:               """, file_name, """
[*] User Agent:              GothBuster/2.0
===============================================================
		""")

def request(target_url):
	try:
		return requests.get("http://" + target_url)
	except requests.exceptions.ConnectionError:
		pass

with open(file_name) as f:
    wordlist = f.read().splitlines()

directories = []
for line in tqdm(wordlist, desc="Processing", unit="phantom directory"):
	try:
		directory = line.strip()
		full_url = target_url + '/' + directory
		response = request(full_url)
		if response:
			directories.append(f'{full_url}')
	except:
		pass

#Print directories
print(termcolor.colored((f'[+] Discovered Directory At This Path: '), 'green'))
for line in directories:
	print(line)
