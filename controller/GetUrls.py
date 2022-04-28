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
        sections = soup.findAll('section', {'class': typeClass})
        for section in sections:
            if typeClass == 'types':
                rows = section.findAll('div', {'class':'row'})
                for row in rows:
                    info = {}
                    tagA = row.find('a', href=re.compile(f'({self.base_URL + self._brand})(.+)'))
                    href = str(tagA.attrs['href']) if tagA != None else ''
                    if 'spec' in href:
                        info['modelURL'] = href
                        info['fuel'] = str(row.find('div', text=re.compile(r'(F)|(G)')).get_text())
                        info['cambio'] = str(row.find('div', text=re.compile(r'(Manual)|(Automatic)')).get_text())
                        info['modelCar'] = str(row.find('a', href=re.compile(f'({self.base_URL + self._brand})(.+)')).attrs['title'])
                        listModelsPag.append(info)
                    else:
                        continue

            else:
                models = section.findAll('a', href=re.compile(f'({self.base_URL + self._brand})(.+)'))
                for model in models:
                    info = {}
                    info['modelURL'] = model.attrs['href']
                    info['fuel'] = None
                    info['cambio'] = None
                    listModelsPag.append(info)
        return listModelsPag


    def getSubModels(self, listUrlsModels, typeClass):
        listSubModels = []
        for urlSubModel in listUrlsModels:
            listSubModels.append(self.getUrl(urlSubModel['modelURL'], typeClass))

        return [item for sublist in listSubModels for item in sublist]


    def generteSubEspec(self, vetDicInfo):
        for dicInfo in vetDicInfo:
            listSubEspec = ['tech', 'sizes', 'options']
            dicInfo['urlEspecs'] = [dicInfo['modelURL'] + '/' + espc for espc in listSubEspec]

        return vetDicInfo

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
    
    @staticmethod
    def extractModelByURL(url):
        return url.split('/')[4].split('-specs')[0]


    def execute(self):
        pag1Urls = self.getUrl(self.base_URL + self._brand, 'models')
        pag2Urls = self.getSubModels(pag1Urls, 'models')
        pag3Urls = self.getSubModels(pag2Urls, 'types')
        return self.generteSubEspec(pag3Urls)


if __name__ == '__main__':
    x = GetModelUrls('abarth')

    vet1 = x.getUrl('https://www.cars-data.com/en/abarth','models')
    vet2 = x.getSubModels(vet1,'models')
    vet3 = x.getSubModels(vet2,'types')
    dicInfo = x.generteSubEspec(vet3)
    for i in dicInfo:
        print('\n')
        print(dicInfo)