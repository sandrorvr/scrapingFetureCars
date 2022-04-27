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
            elif self.titles[self.tabNow] == 'DRIVE':
                obj = TableDrive(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'FUEL ENGINE':
                obj = TableFuelEngine(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'PERFORMANCE':
                obj = TablePerformance(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CONSUMPTION (NEDC)':
                obj = TableConsumptionNEDC(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CONSUMPTION (WLTP)':
                obj = TableConsumptionWLTP(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CHASSIS':
                obj = TableChassis(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'TRANSMISSION':
                obj = TableTransmission(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'WEIGHTS':
                obj = TableWeights(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'LUGGAGE / LOAD COMPARTMENT':
                obj = TableLuggageLoadCompartment(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'EXTERIOR SIZES':
                obj = TableExteriorSizes(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'INTERIOR SIZES':
                obj = TableInteriorSizes(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'SAFETY':
                obj = TableSafety(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'COMFORT':
                obj = TableConfort(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'INTERIOR':
                obj = TableInterior(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'EXTERIOR':
                obj = TableExterior(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'SERVICE & WARRANTY':
                obj = TableServiceWarranty(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'PRICES / VAT / BPM':
                obj = TablePricesVatBpm(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'NEW PRICE HISTORY':
                obj = TableNewPriceHistory(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'OCCASION PRICES':
                obj = TableOccasionPrices(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'COSTS PER MONTH (4 YEARS / 15,000 KM P.J.)':
                obj = TableCostsPerMonth(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            else:
                raise ValueError('EITA PORRA TABELA NAO ENCONTRADA')

        self.tabNow += 1
        return obj
    
    def save(self):
        for _ in range(self.sizeTbs):
            tab = self.getTabNow()
            if tab != None:
                try:
                    self.db.addData(tab)
                except:
                    print(f'tabela erro: {tab.title}')
                    print(tab.getValues())

            

    

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

class TableDrive(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO drive (
            driveWheel,
            engineMotorType,
            fuelType,
            power,
            totalMaxPowerKW,
            totalMaxPowerHp,
            maxTorque,
            brand
            ) VALUES (?,?,?,?,?,?,?,?)'''


class TableFuelEngine(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO fuelEngine (
            cylinders,
            valvesPerCylinder,
            engineCapacity,
            boreStroke,
            compressionRatio,
            maxPower,
            powerKW,
            powerPH,
            maxPowerRpm,
            maxTorque,
            maxTorqueRpm,
            fuelSystem,
            valveActuation,
            turbo,
            catalyst,
            fuelTank,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TablePerformance(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO performance (
            Top,
            Acceleration,
            practiceConsumptionMonitor,
            brand
            ) VALUES (?,?,?,?)'''

class TableConsumptionWLTP(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO consumptionWLTP (
            lowConsumption,
            mediumConsumption,
            highConsumption,
            veryHigh,
            combinedConsumption,
            co2Emissions,
            batteryRange,
            powerConsumption,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?)'''

class TableConsumptionNEDC(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO consumptionNEDC (
            urbanConsumption,
            extraUrbanConsumption,
            combinedConsumption,
            co2Emissions,
            energyLabel,
            powerConsumption,
            batteryRange,
            brand
            ) VALUES (?,?,?,?,?,?,?,?)'''

class TableChassis(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO chassis (
            frontSuspension1,
            rearSuspension1,
            frontSuspension2,
            rearSuspension2,
            frontStabilizer,
            rearStabilizer,
            frontBrakes,
            rearBrakes,
            frontTireSize,
            rearTireSize,
            turningCircle,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableTransmission(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO transmission (
            gear1,
            gear2,
            gear3,
            gear4,
            gear5,
            gear6,
            gear7,
            gear8,
            gear9,
            reverseGear,
            finalDrive,
            RpmAt120Km,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableWeights(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO weights (
            curbWeight,
            maxPayload,
            maxPermissibleMass,
            maxFrontAxleMass,
            maxRearAxleMass,
            maxBrakedTrailerMass,
            maxUnbrakedTrailerMass,
            maxNoseWeight,
            maxRoofLoad,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?)'''

class TableLuggageLoadCompartment(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO luggageLoadCompartment (
            cargoCapacity,
            lengthMinmax,
            widthMinmax,
            height,
            heightLiftThreshold,
            brand
            ) VALUES (?,?,?,?,?,?)'''

class TableExteriorSizes(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO exteriorSizes (
            length,
            width,
            height,
            wheelbase,
            frontTrack,
            rearTrack,
            groundClearance,
            brand
            ) VALUES (?,?,?,?,?,?,?,?)'''


class TableInteriorSizes(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO interiorSizes (
            DistanceBackrestPedals,
            FrontHeadroom,
            FrontBackrestLength,
            FrontSeatLength,
            FrontEntryHeight,
            FrontInteriorWidth,
            DistanceBackrestFrontRear,
            avgDistanceBackrestFrontRear,
            RearHeadroom,
            BackrestLength,
            RearSeatLength,
            RearSeatHeight,
            RearInteriorWidth,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''


class TableSafety(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO safety (
            crashTestResult,
            aBS,
            brakeForceDistribution,
            brakeAssist,
            emergencyBrakingAssistance,
            blindSpotAssist,
            stabilityControl,
            tractionControl,
            limitedSlipDifferential,
            driversAirbag,
            passengerAirbag,
            sideAirbags,
            headCurtainAirbags,
            driversKneeAirbag,
            hillAssist,
            laneAssist,
            blindSpotAssistant,
            fatigueSensor,
            tirePressureSensor,
            citySafetySystem,
            nightVisionWithPersonRecognition,
            precrashSystem,
            highBeamAssistant,
            trafficSignRecognition,
            collisionWarningSystem,
            automaticLevelControl,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableConfort(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO confort (
            centralDoorLocking,
            keylessEntryStart,
            startButton,
            controlCircuit,
            electricWindows,
            powerSteering,
            cruiseControl,
            airConditioning,
            leftRightTemperatureControl,
            parkingSensors,
            reverseCamera,
            parkingMachine,
            electricParkingBrake,
            startStopSystem,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableInterior(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO interior (
            heightAdjustmentSeat,
            lumbarSupportSeat,
            electricAdjustmentSeat,
            heatedSeats,
            ventilatedSeats,
            sportsSeats,
            leatherCoveredSteeringWheel,
            adjustableSteeringWheel,
            heatedSteeringWheel,
            leatherUpholstery,
            rearHeadrests,
            foldingRearSeats,
            slidingRearSeat,
            centerArmrest,
            automaticallyDimmingInteriorMirror,
            readingLamps,
            illuminatedMakeupMirror,
            adjustableDashboardLighting,
            tachometer,
            dayCounter,
            coolingWaterTemperatureGauge,
            outsideTemperatureGauge,
            boardComputer,
            audioSystem,
            digitalRadioDAB,
            steeringWheelControlsForAudio,
            audioInput,
            navigationSystem,
            bluetooth,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableExterior(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO exterior (
            IntervalWiper,
            AlloyWheels,
            SlidingTiltingRoof,
            PanoramicRoof,
            RoofRails,
            MetallicPaint,
            PaintedBumpers,
            TintedGlass,
            RearPrivacyGlass,
            ElectricMirrors,
            FoldingExteriorMirrors,
            AutomaticallyDimmingExteriorMirrors,
            DirectionIndicatorInExteriorMirrors,
            FrontFogLights,
            AutomaticallySwitchingOnLighting,
            XenonHeadlights,
            LedHeadlights,
            LEDRearLighting,
            DaytimeRunningLights,
            HeadlampWashers,
            BurglarAlarm,
            brand
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableServiceWarranty(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO serviceWarranty (
            service,
            generalWarranty,
            bodyWarranty,
            brand
            ) VALUES (?,?,?,?)'''

class TablePricesVatBpm(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO pricesVatBpm (
            newPriceTax,
            newPriceRoadworthy,
            brand
            ) VALUES (?,?,?)'''


class TableNewPriceHistory(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO newPriceHistory (
            newPrice2019,
            newPrice2018,
            newPrice2017,
            newPrice2016,
            brand
            ) VALUES (?,?,?,?,?)'''

class TableOccasionPrices(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO occasionPrices (
            occasionPrice2019,
            occasionPrice2018,
            occasionPrice2017,
            occasionPrice2016,
            brand
            ) VALUES (?,?,?,?,?)'''

class TableCostsPerMonth(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO costsPerMonth (
            years4Depreciation,
            motorVehicleTax,
            insurance,
            fuelCosts,
            maintenance,
            totalCosts,
            totalCostsPerKilometer,
            brand
            ) VALUES (?,?,?,?,?,?,?,?)'''
