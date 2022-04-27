import bs4
import requests
import re
import pandas as pd


class GetModelUrls:

    base_URL = 'https://www.cars-data.com/en/'

    def __init__(self, brand):
        self._brand = brand

    def getUrl(self, url: str, typeClass: str) -> list:
        listModelsPag = []
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        sectionModels = soup.findAll('section', {'class': typeClass})

        for sectionModel in sectionModels:
            models = sectionModel.findAll('a', href=re.compile(
                f'({self.base_URL + self._brand})(.+)'))
            for mdl in models:
                href = str(mdl.attrs['href'])
                if typeClass == 'types' and 'spec' in href:
                    listModelsPag.append(href)
                else:
                    listModelsPag.append(href)

        return listModelsPag

    def getSubModels(self, listUrlsModels, typeClass):
        listSubModels = []
        for urlSubModel in listUrlsModels:
            listSubModels.append(self.getUrl(urlSubModel, typeClass))

        return [item for sublist in listSubModels for item in sublist]

    def getSpec(self, urls):
        return [self.generteSubEspec(url) for url in urls if 'spec' in url]

    def generteSubEspec(self, url):
        listSubEspec = ['tech', 'sizes', 'options']
        new_url = []
        for el in listSubEspec:
            new_url.append(url+'/'+el)

        return new_url

    @classmethod
    def getTables(cls, url):
        res = requests.get(url)
        tabs = pd.read_html(res.text)
        return tabs

    @classmethod
    def getTitleTB(cls, url):
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        titles = soup.select('th > h2')
        return [h2.text for h2 in titles]

    def execute(self):
        pag1Urls = self.getUrl(self.base_URL + self._brand, 'models')
        pag2Urls = self.getSubModels(pag1Urls, 'models')
        pag3Urls = self.getSubModels(pag2Urls, 'types')
        return self.getSpec(pag3Urls)


