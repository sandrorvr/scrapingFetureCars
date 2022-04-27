import sqlite3


class DB:
    _instance = None

    def __init__(self, db):
        self.db = db
        self.conn = None

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
        cursor.execute('''CREATE TABLE drive (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            driveWheel TEXT,
                            engineMotorType TEXT,
                            fuelType TEXT,
                            power TEXT,
                            totalMaxPowerKW INTEGER,
                            totalMaxPowerHp INTEGER,
                            maxTorque TEXT,
                            brand TEXT);''')

        cursor.execute('''CREATE TABLE fuelEngine (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            cylinders TEXT,
                            valvesPerCylinder INTEGER,
                            engineCapacity TEXT,
                            boreStroke TEXT,
                            compressionRatio INTEGER,
                            maxPower INTEGER,
                            powerKW INTEGER,
                            powerPH INTEGER,
                            maxPowerRpm TEXT,
                            maxTorque TEXT,
                            maxTorqueRpm TEXT,
                            fuelSystem TEXT,
                            valveActuation TEXT,
                            turbo TEXT,
                            catalyst TEXT,
                            fuelTank Capacity TEXT,
                            brand TEXT);''')

        cursor.execute('''CREATE TABLE general (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            price TEXT,newPriceRoadworthy TEXT,
                            roadTax3Months TEXT,bodyType TEXT,
                            transmission TEXT,
                            numberOfSeats INTEGER,
                            segment TEXT,
                            introduction TEXT,
                            end TEXT, 
                            brand TEXT);''')

        cursor.execute('''CREATE TABLE performance (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Top Speed TEXT,
                            Acceleration TEXT,
                            practiceConsumptionMonitor TEXT,
                            brand TEXT);''')

        cursor.execute('''CREATE TABLE consumption (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            brand TEXT,
                            lowConsumption TEXT,
                            mediumConsumption TEXT,
                            highConsumption TEXT,
                            veryHigh Consumption TEXT,
                            combinedConsumption TEXT,
                            co2Emissions TEXT,
                            batteryRange TEXT,
                            powerConsumption TEXT,
                            )''')
        
        cursor.execute('''CREATE TABLE chassis (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            brand TEXT,
                            frontSuspension TEXT,
                            rearSuspension TEXT,
                            frontSuspension TEXT,
                            rearSuspension TEXT,
                            frontStabilizer TEXT,
                            rearStabilizer TEXT,
                            frontBrakes TEXT,
                            rearBrakes TEXT,
                            frontTireSize TEXT,
                            rearTireSize TEXT,
                            turningCircle TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE transmission (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            brand TEXT,
                            gear1 TEXT,
                            gear2 TEXT,
                            gear3 TEXT,
                            gear4 TEXT,
                            gear5 TEXT,
                            gear6 TEXT,
                            gear7 TEXT,
                            gear8 TEXT,
                            gear9 TEXT,
                            reverseGear TEXT,
                            finalDrive TEXT,
                            RpmAt120Km TEXT,
                            )''')

        self.conn.commit()
        self.conn.close()
    
    def addData(self, tab):
        queryInsert = tab.getInsertGuery()
        values = tab.getValues()
        cursor = self.connect()
        cursor.execute(queryInsert,values)
        self.conn.commit()
        self.conn.close()
