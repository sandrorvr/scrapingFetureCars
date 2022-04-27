from abc import ABC, abstractclassmethod
import pandas as pd
import os

from model.DB import DB


class Tables:
    def __init__(self, brand, espec, tabs, titles):
        self.db = DB.createInstace('DataBase.db')
        self.brand = brand
        self.tabs = tabs
        self.espec = espec
        self.titles = titles
        self.sizeTbs = len(tabs)
        self.tabNow = 0
        self.verification()#DB.createInstace('./DB/DataBase.db')

    def verification(self):
        if self.sizeTbs != len(self.titles):
            print(self.sizeTbs, len(self.titles)) 
            raise ValueError('Numero de titulos diferente do numero de tabelas')
        if not os.path.exists('DataBase.db'):
            self.db.createDB()
        
    
    def getTabNow(self):
        obj = None
        if self.tabNow < self.sizeTbs:
            if self.titles[self.tabNow] == 'GENERAL':
                obj = TableGeneral(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
        self.tabNow += 1
        return obj
    
    def save(self):
        for _ in range(self.sizeTbs):
            tab = self.getTabNow()
            if tab != None:
                self.db.addData(tab)
            

    

class TableAbstract(ABC):
    def __init__(self,table, brand, espec, title):
        self.brand = brand
        self.table = table
        self.espec = espec
        self.title = title
    
    
    def transformTable(self):
        self.table.columns = ['feture', 'info']
        return pd.DataFrame(self.table.set_index(self.table['feture']).loc[:, 'info']).T
    
    
    def getValues(self):
        self.table.columns = ['feture', 'info']
        values = list(self.table['info'].values)
        values.append(self.brand)
        return values
    

    @abstractclassmethod
    def getInsertGuery(self):
        pass


class TableGeneral(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO general (
            price,
            newPriceRoadworthy,
            roadTax3Months,
            bodyType,
            transmission,
            numberOfSeats,
            segment,
            introduction,
            end,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?)'''