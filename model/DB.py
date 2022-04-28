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
        #tables TECH
        cursor.execute('''CREATE TABLE drive (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            driveWheel TEXT,
                            engineMotorType TEXT,
                            fuelType TEXT,
                            power TEXT,
                            totalMaxPowerKW INTEGER,
                            totalMaxPowerHp INTEGER,
                            maxTorque TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

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
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE general (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            price TEXT,
                            newPriceRoadworthy TEXT,
                            roadTax3Months TEXT,
                            bodyType TEXT,
                            transmission TEXT,
                            numberOfSeats INTEGER,
                            segment TEXT,
                            introduction TEXT,
                            end TEXT, 
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE performance (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Top Speed TEXT,
                            Acceleration TEXT,
                            practiceConsumptionMonitor TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE consumptionNEDC (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            urbanConsumption TEXT,
                            extraUrbanConsumption TEXT,
                            combinedConsumption TEXT,
                            co2Emissions TEXT,
                            energyLabel TEXT,
                            powerConsumption TEXT,
                            batteryRange TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE consumptionWLTP (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            lowConsumption TEXT,
                            mediumConsumption TEXT,
                            highConsumption TEXT,
                            veryHigh Consumption TEXT,
                            combinedConsumption TEXT,
                            co2Emissions TEXT,
                            batteryRange TEXT,
                            powerConsumption TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE chassis (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            frontSuspension1 TEXT,
                            rearSuspension1 TEXT,
                            frontSuspension2 TEXT,
                            rearSuspension2 TEXT,
                            frontStabilizer TEXT,
                            rearStabilizer TEXT,
                            frontBrakes TEXT,
                            rearBrakes TEXT,
                            frontTireSize TEXT,
                            rearTireSize TEXT,
                            turningCircle TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE transmission (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        #tables SIZES
        cursor.execute('''CREATE TABLE weights (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            curbWeight TEXT,
                            maxPayload TEXT,
                            maxPermissibleMass TEXT,
                            maxFrontAxleMass TEXT,
                            maxRearAxleMass TEXT,
                            maxBrakedTrailerMass TEXT,
                            maxUnbrakedTrailerMass TEXT,
                            maxNoseWeight TEXT,
                            maxRoofLoad TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE luggageLoadCompartment (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            cargoCapacity TEXT,
                            lengthMinmax TEXT,
                            widthMinmax TEXT,
                            height TEXT,
                            heightLiftThreshold TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE exteriorSizes (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            length TEXT,
                            width TEXT,
                            height TEXT,
                            wheelbase TEXT,
                            frontTrack Width TEXT,
                            rearTrack Width TEXT,
                            groundClearance TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE interiorSizes (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            DistanceBackrestPedals TEXT,
                            FrontHeadroom TEXT,
                            FrontBackrestLength TEXT,
                            FrontSeatLength TEXT,
                            FrontEntryHeight TEXT,
                            FrontInteriorWidth TEXT,
                            DistanceBackrestFrontRear TEXT,
                            avgDistanceBackrestFrontRear TEXT,
                            RearHeadroom TEXT,
                            BackrestLength TEXT,
                            RearSeatLength TEXT,
                            RearSeatHeight TEXT,
                            RearInteriorWidth TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        #Tables OPTIONS
        cursor.execute('''CREATE TABLE safety (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            crashTestResult TEXT,
                            aBS TEXT,
                            brakeForceDistribution TEXT,
                            brakeAssist TEXT,
                            emergencyBrakingAssistance TEXT,
                            blindSpotAssist TEXT,
                            stabilityControl TEXT,
                            tractionControl TEXT,
                            limitedSlipDifferential TEXT,
                            driversAirbag TEXT,
                            passengerAirbag TEXT,
                            sideAirbags TEXT,
                            headCurtainAirbags TEXT,
                            driversKneeAirbag TEXT,
                            hillAssist TEXT,
                            laneAssist TEXT,
                            blindSpotAssistant TEXT,
                            fatigueSensor TEXT,
                            tirePressureSensor TEXT,
                            citySafetySystem TEXT,
                            nightVisionWithPersonRecognition TEXT,
                            precrashSystem TEXT,
                            highBeamAssistant TEXT,
                            trafficSignRecognition TEXT,
                            collisionWarningSystem TEXT,
                            automaticLevelControl TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE confort (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            centralDoorLocking TEXT,
                            keylessEntryStart TEXT,
                            startButton TEXT,
                            controlCircuit TEXT,
                            electricWindows TEXT,
                            powerSteering TEXT,
                            cruiseControl TEXT,
                            airConditioning TEXT,
                            leftRightTemperatureControl TEXT,
                            parkingSensors TEXT,
                            reverseCamera TEXT,
                            parkingMachine TEXT,
                            electricParkingBrake TEXT,
                            startStopSystem TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE interior (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            heightAdjustmentSeat TEXT,
                            lumbarSupportSeat TEXT,
                            electricAdjustmentSeat TEXT,
                            heatedSeats TEXT,
                            ventilatedSeats TEXT,
                            sportsSeats TEXT,
                            leatherCoveredSteeringWheel TEXT,
                            adjustableSteeringWheel TEXT,
                            heatedSteeringWheel TEXT,
                            leatherUpholstery TEXT,
                            rearHeadrests TEXT,
                            foldingRearSeats TEXT,
                            slidingRearSeat TEXT,
                            centerArmrest TEXT,
                            automaticallyDimmingInteriorMirror TEXT,
                            readingLamps TEXT,
                            illuminatedMakeupMirror TEXT,
                            adjustableDashboardLighting TEXT,
                            tachometer TEXT,
                            dayCounter TEXT,
                            coolingWaterTemperatureGauge TEXT,
                            outsideTemperatureGauge TEXT,
                            boardComputer TEXT,
                            audioSystem TEXT,
                            digitalRadioDAB TEXT,
                            steeringWheelControlsForAudio TEXT,
                            audioInput TEXT,
                            navigationSystem TEXT,
                            bluetooth TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE exterior (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            IntervalWiper TEXT,
                            AlloyWheels TEXT,
                            SlidingTiltingRoof TEXT,
                            PanoramicRoof TEXT,
                            RoofRails TEXT,
                            MetallicPaint TEXT,
                            PaintedBumpers TEXT,
                            TintedGlass TEXT,
                            RearPrivacyGlass TEXT,
                            ElectricMirrors TEXT,
                            FoldingExteriorMirrors TEXT,
                            AutomaticallyDimmingExteriorMirrors TEXT,
                            DirectionIndicatorInExteriorMirrors TEXT,
                            FrontFogLights TEXT,
                            AutomaticallySwitchingOnLighting TEXT,
                            XenonHeadlights TEXT,
                            LedHeadlights TEXT,
                            LEDRearLighting TEXT,
                            DaytimeRunningLights TEXT,
                            HeadlampWashers TEXT,
                            BurglarAlarm TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE serviceWarranty (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            service TEXT,
                            generalWarranty TEXT,
                            bodyWarranty TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE pricesVatBpm (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            newPriceTax TEXT,
                            newPriceRoadworthy TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')

        cursor.execute('''CREATE TABLE newPriceHistory (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            newPrice2019 TEXT,
                            newPrice2018 TEXT,
                            newPrice2017 TEXT,
                            newPrice2016 TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE occasionPrices (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            occasionPrice2019 TEXT,
                            occasionPrice2018 TEXT,
                            occasionPrice2017 TEXT,
                            occasionPrice2016 TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
                            )''')
        
        cursor.execute('''CREATE TABLE costsPerMonth (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            years4Depreciation TEXT,
                            motorVehicleTax TEXT,
                            insurance TEXT,
                            fuelCosts TEXT,
                            maintenance TEXT,
                            totalCosts TEXT,
                            totalCostsPerKilometer TEXT,
                            brand TEXT,
                            modelCar TEXT,
                            fuel TEXT,
                            cambio TEXT
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
