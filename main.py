from controller.GetUrls import GetModelUrls
from model.Tables import Tables

if __name__ == '__main__':

    brand = 'abarth'

    urls = GetModelUrls(brand).execute()
    for i in range(len(urls)):
        for espec,url in enumerate(urls[i]):
            print(url)
            tabs = GetModelUrls.getTables(url)
            titles = GetModelUrls.getTitleTB(url)
            Tables(brand, espec, tabs, titles).save()
            
