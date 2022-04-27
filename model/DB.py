import sqlite3


class DB:
    _instance = None

    def __init__(self, db):
        self.db = db
        self.conn = None
        print(db)

    @classmethod
    def createInstace(cls, db):
        if cls._instance == None:
            cls._instance = cls(db)
        return cls._instance

    def close(self):
        self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn.cursor()


    def createDB(self):
        cursor = self.connect()
        cursor.execute('CREATE TABLE drive (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,driveWheel TEXT,engineMotorType TEXT,fuelType TEXT,power TEXT,totalMaxPowerKW INTEGER,totalMaxPowerHp INTEGER,maxTorque TEXT,brand TEXT);')
        cursor.execute('CREATE TABLE fuelEngine (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,cylinders TEXT,valvesPerCylinder INTEGER,engineCapacity TEXT,boreStroke TEXT,compressionRatio INTEGER,maxPower INTEGER,powerKW INTEGER,powerPH INTEGER,maxPowerRpm TEXT,maxTorque TEXT,maxTorqueRpm TEXT,fuelSystem TEXT,valveActuation TEXT,turbo TEXT,catalyst TEXT,fuelTank Capacity TEXT,brand TEXT);')
        cursor.execute('CREATE TABLE general (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,price TEXT,newPriceRoadworthy TEXT,roadTax3Months TEXT,bodyType TEXT,transmission TEXT,numberOfSeats INTEGER,segment TEXT,introduction TEXT,end TEXT, brand TEXT);')
        cursor.execute('CREATE TABLE performance (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,Top Speed TEXT,Acceleration TEXT,practiceConsumptionMonitor TEXT,brand TEXT);')
        self.conn.commit()
        self.conn.close()
    
    def addData(self, tab):
        queryInsert = tab.getInsertGuery()
        values = tab.getValues()
        print(values, '<<<<')
        cursor = self.connect()
        cursor.execute(queryInsert,values)
        self.conn.commit()
        self.conn.close()
