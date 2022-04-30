from abc import ABC, abstractclassmethod
from numpy import full_like
import pandas as pd
import os
import json

from model.DB import DB


class Tables:
    def __init__(self, brand, modelCar,fuel, cambio, espec, tabs, titles):
        self.db = DB.createInstace('DataBase.db')
        self.brand = brand
        self.modelCar = modelCar
        self.fuel = fuel
        self.cambio = cambio
        self.tabs = tabs
        self.espec = espec
        self.titles = titles
        self.sizeTbs = len(tabs)
        self.tabNow = 0
        self.verification()

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
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'DRIVE':
                obj = TableDrive(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'FUEL ENGINE':
                obj = TableFuelEngine(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'PERFORMANCE':
                obj = TablePerformance(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CONSUMPTION (NEDC)':
                obj = TableConsumptionNEDC(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CONSUMPTION (WLTP)':
                obj = TableConsumptionWLTP(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'CHASSIS':
                obj = TableChassis(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'TRANSMISSION':
                obj = TableTransmission(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'WEIGHTS':
                obj = TableWeights(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'LUGGAGE / LOAD COMPARTMENT':
                obj = TableLuggageLoadCompartment(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'EXTERIOR SIZES':
                obj = TableExteriorSizes(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'INTERIOR SIZES':
                obj = TableInteriorSizes(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'SAFETY':
                obj = TableSafety(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'COMFORT':
                obj = TableConfort(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'INTERIOR':
                obj = TableInterior(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'EXTERIOR':
                obj = TableExterior(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'SERVICE & WARRANTY':
                obj = TableServiceWarranty(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'PRICES / VAT / BPM':
                obj = TablePricesVatBpm(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'NEW PRICE HISTORY':
                obj = TableNewPriceHistory(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'OCCASION PRICES':
                obj = TableOccasionPrices(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            elif self.titles[self.tabNow] == 'COSTS PER MONTH (4 YEARS / 15,000 KM P.J.)':
                obj = TableCostsPerMonth(
                    self.tabs[self.tabNow],
                    self.brand, 
                    self.modelCar,
                    self.fuel,
                    self.cambio,
                    self.espec, 
                    self.titles[self.tabNow]
                    )
            else:
                with open('log.json','a') as file:
                    erro = {
                            'erro': 'table not find', 
                            'brand': self.brand, 
                            'modelCar': self.modelCar,
                            'fase': '[find table > fase2]'
                            }
                    json.dump(erro, file)
                    file.write(',\n')

        self.tabNow += 1
        return obj
    
    def save(self):
        for _ in range(self.sizeTbs):
            tab = self.getTabNow()
            if tab != None:
                try:
                    self.db.addData(tab)
                except Exception as erro:
                    logErro = {
                        'erro': erro.args,
                        'fase': '[save > fase2]',
                        'table': tab.title,
                    }
                    with open('log.json','a') as file:
                        json.dump(logErro, file)
                        file.write(',\n')

            
class TableAbstract(ABC):
    def __init__(self,table, brand, modelCar,fuel, cambio, espec, title):
        self.brand = brand
        self.modelCar = modelCar
        self.fuel = fuel
        self.cambio = cambio
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
        values.append(self.modelCar)
        values.append(self.fuel)
        values.append(self.cambio)
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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''


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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TablePerformance(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO performance (
            Top,
            Acceleration,
            practiceConsumptionMonitor,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableLuggageLoadCompartment(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO luggageLoadCompartment (
            cargoCapacity,
            lengthMinmax,
            widthMinmax,
            height,
            heightLiftThreshold,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''


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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''


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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

class TableServiceWarranty(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO serviceWarranty (
            service,
            generalWarranty,
            bodyWarranty,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?)'''

class TablePricesVatBpm(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO pricesVatBpm (
            newPriceTax,
            newPriceRoadworthy,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?)'''


class TableNewPriceHistory(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO newPriceHistory (
            newPrice2019,
            newPrice2018,
            newPrice2017,
            newPrice2016,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?)'''

class TableOccasionPrices(TableAbstract):
    def getInsertGuery(self):
        return '''INSERT INTO occasionPrices (
            occasionPrice2019,
            occasionPrice2018,
            occasionPrice2017,
            occasionPrice2016,
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?)'''

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
            brand,
            modelCar,
            fuel,
            cambio
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
