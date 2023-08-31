# dolistore-scrapping
Outils en python récupérant les versions de mes modules, le nombre de vente et la date de la dernière vente


Le premier permet de récupérer les versions des modules présents dans un fichier dolistore_modules_url.txt

le format du fichier est le suivant :

        Factory=https://www.dolistore.com/fr/gestion-produits-ou-services/386-Factory---la-GPAO-avanc--e-pour-Dolibarr.html
        
        Mydoliboard=https://www.dolistore.com/fr/reporting-ou-recherche/316-MyDoliboard---tableaux-de-bord-personnalis--s.html

Il récupère la version du module, la version mininum de dolibarr et la version maximum de dolibarr sous ce format

NomModule        versionModule        versionMax           versionMin

Factory           3.2.2                17.0.x               12.0.x

Mydoliboard       3.9.0                16.0.x               10.0.x



Le second est pour les développeur
il est probable que ce programme soit adaptable à toute les boutiques prestashop, mais je n'ai pas fait de test en ce sens (feedback welcome)
Exemple de l'affichage généré : 

        myDiscount      17.0.x  16      15/06/2019      14/12/2022      42     4
        MyDoliboard     16.0.x  177     01/12/2013      12/01/2023      110    19
        myDolidash      16.0.0  3       02/10/2022      30/01/2023      4      9
        myField         17.0.x  653     14/05/2015      22/04/2023      96     81
        myList          17.0.x  533     20/09/2013      19/04/2023      116    54
        myPrint         15.0.x  60      17/10/2016      14/04/2023      79     9
        mySchedule      17.0.x  24      22/05/2021      01/04/2023      22     12
        Periodic        15.0.x  25      24/10/2017      10/02/2023      64     4
        Portofolio      17.0.x  99      15/09/2015      07/02/2023      90     13
        Process         16.0.x  101     24/06/2013      02/03/2023      117    10
        projectbudget   17.0.x  51      14/05/2017      14/04/2023      72     8
        reStock         17.0.x  234     26/03/2014      27/03/2023      109    25

- Nombre de modules avec version 15 : 2
- Nombre de modules avec version 16 : 5
- Nombre de modules avec version 17 : 30

- Nb modules dans l'année 2012 : 1
- Nb modules dans l'année 2013 : 3
- Nb modules dans l'année 2014 : 8
- ../.. 
- Nb modules dans l'année 2017 : 4
- Nb modules dans l'année 2018 : 2
- Nb modules dans l'année 2019 : 3

- Nombre de modules total: 37
- Nombre de ventes total: xxxxx
