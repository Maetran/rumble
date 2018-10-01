import urllib.request
import bs4
import re
dicPages = {1 : "https://www.switzerland.org/internet/ip-adresse.de",\
            2 : "http://www.wieistmeineip.ch",\
            3 : "http://www.dnstools.ch/wie-ist-meine-ip.html"}

def myIP(webseite):
    link = urllib.request.urlopen(webseite)
    soup = bs4.BeautifulSoup(link, 'html.parser')
    text = soup.get_text()
    IP = re.findall(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", text)
    IP = IP[0]
    return IP

print("Welchen Anbieter?")
for key in dicPages:
    print(str(key) + ": " + str(dicPages[key]))

choise = int(input("Wählen von 1-3: "))
ip = myIP(dicPages[choise])
print("Deine WAN-IP ist:", ip)
