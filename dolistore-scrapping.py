#  Copyright (C) 2022-2023 charlene Benke  <charlene@patas-monkey.com>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.


from datetime import datetime, timedelta
import mechanize, http
from bs4 import BeautifulSoup


## récupération des infos sur le dolistore
cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
#br.set_cookiejar(cj)

br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open("https://www.dolistore.com/fr/authentification")
br.select_form(id="login_form")
br.form['email'] = 'xxxxxxx'
br.form['passwd'] = 'xxxxxx'
br.submit()

# on se positionne ensuite sur la page des produits
result = br.open("https://www.dolistore.com/fr/module/blockmysales/manageproduct")
html = br.response().read()
soup = BeautifulSoup(html, features="lxml")
table = soup.find(id="manageproduct_productlist")

nbTotal=0
nbVenteTotal=0
ArrayVersion = {}
ArrayPhpVersion = {}
ArrayYearCreate = {}

# on récupère les informations du modules sur le dolistore
for row in table.findAll('tr')[1:]: 
	nbVenteDolistore=0
	versionDolistore=""

	col = row.findAll('td')
	moduleName= col[1].findAll('a')
	# si le module a : dans le nom il est en activité
	separation = moduleName[0].text.split(" : ")
	if (len(separation) == 2):
		nbTotal=nbTotal+1
		nbVenteCell = col[2].findAll('a')
		# on récupère l'url du href
		versionDolistore = separation[1].split(" - ")[1]
		ArrayVersion[versionDolistore[:2]] = ArrayVersion.get(versionDolistore[:2], 0) + 1
		nbVenteDolistore = nbVenteCell[0].text
		nbVenteTotal = nbVenteTotal + int(nbVenteDolistore)
		# on se positionne pour aller sur l'onglet des ventes
		result = br.open(nbVenteCell[0].get('href'))
		htmlVente = br.response().read()
		soupVente = BeautifulSoup(htmlVente, features="lxml")
		divVente = soupVente.find(id="productcard_tabs-1")
		ListVente = divVente.findAll("table")[0].findAll("tr")[1:]
		FirstVente = ListVente[1]
		FirstVenteDate = FirstVente.findAll("td")[3].text
		dateFirstVente = datetime.strptime(FirstVenteDate, "%d/%m/%Y %H:%M:%S")
		ArrayYearCreate[dateFirstVente.year] = ArrayYearCreate.get(dateFirstVente.year, 0) + 1
		LastVente = ListVente[len(ListVente )-2] # la derniere ligne c'est le total...
		LastVenteDate = LastVente.findAll("td")[3].text
		dateLastVente = datetime.strptime(LastVenteDate, "%d/%m/%Y %H:%M:%S")
		# Vérifier si la différence est supérieure à six mois
		moduleName = separation[0]
		if (datetime.now() - dateLastVente) > timedelta(days=180):
			moduleName = "\t" + separation[0]
		nbMoisVente = (dateLastVente - dateFirstVente).days/30
		ratioMens = 0
		if nbMoisVente != 0:
			ratioMens = int(nbVenteDolistore)/(nbMoisVente/12)
		print (moduleName + " " + versionDolistore + " " + nbVenteDolistore + " " + FirstVenteDate + " " + LastVenteDate + " " + str(int(nbMoisVente)) + " " + str(int(ratioMens)) )


# on affiche le nombre de module par version de dolibarr
for Version, nombre in dict(sorted(ArrayVersion.items())).items():
	print ("Nombre de modules avec version "+str(Version)+" : "+str(nombre))


for Version, nombre in dict(sorted(ArrayYearCreate.items())).items():
	print ("Nb modules dans l'année "+str(Version)+" : "+str(nombre))

print ("Nombre de modules total: "+str(nbTotal))
print ("Nombre de ventes total: "+str(nbVenteTotal))
