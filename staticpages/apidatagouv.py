import requests
import json
import time
from datetime import datetime


class GouvApiData:
    """ Extrait des données de Open Data en utlisant l'API entreprise data gouv
    """ 

## Documentations  :
# https://entreprise.data.gouv.fr/api_doc_sirene
# https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee
# https://doc.entreprise.api.gouv.fr/#bilans-entreprises-bdf-banque-de-france

    def __init__(self):
        ### Initialization method ###
        self.created = datetime.now()
        self.updated = datetime.now()
        self.url_api = 'https://entreprise.data.gouv.fr/api/sirene/v3/'
        self.headers = ""
        self.response = ""

    def search_active_by_cp(self,code_postal,nb_page_results = 1):
        """ Recherche tous les établissement actifs par code postal

            Arguments :

                code_postal : Code postal écrit avec un STR exemple : '75000'

                nb_page_results : facultatif, valeur par défaut : 1
                        1 : Donne la première page 
                        0 : Donne toutes les pages
        """

        self.nb_page_results = nb_page_results

        # Construction des éléments de la requete  
        self.url_data_type =  'etablissements/'
        self.headers = {
            'Accept': 'application/json',
            }   
        self.url_filter_array = [ 
            '?'
            'etat_administratif=A' ,
            f'code_postal={code_postal}' 
            ]

        # Envois de la requete
        response = self.get_response()

        # Analyse de la requete
        self.analyze_response(response)
        total_results = self.total_results

        # Sauvegarde des résultats dans un JSON
        if self.nb_page_results == 1:
            self.save_in_file(self.response.json())

        # Récupération de tous les résultats nb_page = 
        if self.nb_page_results == 0:
            
            nb_page = self.total_results // 100
            self.response = []
            for page in range(1,nb_page+2):
                self.response += self.get_response(page,100).json()['etablissements']
                time.sleep(1.1)
            
            #self.save_in_file(response)

        return ""

    def search_by_siret(self,siret):
        """ 
        """

        # Construction des éléments de la requete  
        self.url_data_type =  f'etablissements/{siret}/'
        self.headers = {
            'Accept': 'application/json',
            }   
        self.url_filter_array = [
            ]

        # Envois de la requete
        response = self.get_response(0,0)
        return response

    def url_pagination(self,page=0,per_page=0 ):
        """ Retourne la partie pagination de l'URL de la requete
            page : numéro de la page
            per_page : nombre de réponse par page
        """
        url_pagination = ""
        if page != 0:
            url_pagination_array = [
                '&'
                f'page={page}',
                f'per_page={per_page}'
                ]
            url_pagination = "&".join(url_pagination_array)

        return url_pagination
    
    def url_filters(self):

        url_filter_array = ['?'] + self.url_filter_array
 
        if len(url_filter_array) > 1 :
            url_filters = "&".join(self.url_filter_array)
        else: 
            url_filters = ""

        return url_filters

    def get_response(self,page=1,per_page=1):
        """ Retourne les résultats de la requete
        """

        self.url = self.url_api + self.url_data_type + self.url_filters() + self.url_pagination(page,per_page)
        print(self.url)
        self.response = requests.get(self.url, headers=self.headers)
        return self.response
        

    def analyze_response(self,response):
        """ Mets à jours des attributs tels que :
        total_results
        """

        response_meta = response.json()['meta']
        self.total_results = response_meta['total_results']
        self.per_page = response_meta['per_page']
        self.page = response_meta['page']
        self.total_pages = response_meta['total_pages']

    def save_in_file(self):
        """Enregistre dans un JSON les résultats de la requete"""
        content = self.response
        with open(self.resultfilename(), 'w') as outfile:
            json.dump(content, outfile)
            #json.dump(self.response.json()['etablissements'], outfile)

        return 'ok'

    def resultfilename(self):
        """Retourne un nom horodaté pour la fichier résultat
        """ 
        d = datetime.now()
        resultfilename = "./json/"+ "results_" + str(d.year) + "_" + str(d.month) + "_" + str(d.day) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)+".json"
        return resultfilename