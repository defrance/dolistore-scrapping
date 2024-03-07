# avant de lancer le programme, il faut installer les bibliothèques suivantes :
# pip install mechanize
# pip install bs4

import os
import pathlib											

import mechanize
import http
from bs4 import BeautifulSoup

myFolderpath= pathlib.Path(__file__).parent.resolve()	
os.chdir(myFolderpath)									


# on ouvre le fichier contenant les urls
# le format est le suivant :
# nommodule=url
# exemple :
# Factory=https://www.dolistore.com/fr/gestion-produits-ou-services/386-Factory---la-GPAO-avanc--e-pour-Dolibarr.html
# Mydoliboard=https://www.dolistore.com/fr/reporting-ou-recherche/316-MyDoliboard---tableaux-de-bord-personnalis--s.html

with open('dolistore_modules_url.txt', 'r') as f:
    urls = f.readlines()

# on boucle sur les urls
## récupération des infos sur le dolistore
cj = http.cookiejar.CookieJar()
br = mechanize.Browser()

br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

print("NomModule", "\t", "versionModule","\t", "versionMax","\t", "versionMin")
for url in urls:
	NomModule = url.split("=")[0]
	result = br.open(url.split("=")[1])
	html = br.response().read()
	soup = BeautifulSoup(html, features="lxml")
	scripts = soup.find_all("script")
	# le bon scripts est l'avant dernier
	tblScriptContent = str(scripts[-2]).split("=")
	# on découpe le script en 3 parties pour récupérer les infos
	versionModule = tblScriptContent[1].split("\n")[0].replace("'","")
	versionMax = tblScriptContent[2].split("\n")[0].replace("'","")
	versionMin = tblScriptContent[3].split("\n")[0].replace("'","")

	print(NomModule,"\t", versionModule,"\t", versionMax,"\t", versionMin)
