from cmath import log
from controller.GetUrls import GetModelUrls
from model.Tables import Tables
from tqdm import tqdm
import time
import json
import requests


def getLog(dicLog):
	with open('log.json','a') as file:
		json.dump(dicLog, file)
		file.write(',\n')


if __name__ == '__main__':
	#'audi'

	brands = ['abarth','aiways','alfa-romeo','alpine','asia-motors','aston-martin','austin','autobianchi','bentley','bmw','bugatti',
	'buick','cadillac','carver','chevrolet','chrysler','citroen','corvette',
	'cupra','dacia','daewoo','daihatsu','daimler','datsun','dodge','donkervoort',
	'ds','ferrari','fiat','fisker','ford','fso','galloper','honda','hummer',
	'hyundai','infiniti','innocenti','iveco','jaguar','jeep','josse','kia',
	'lada','lamborghini','lancia','land-rover','landwind','lexus','lincoln',
	'lotus','marcos','maserati','maybach','mazda','mclaren','mega','mercedes-benz',
	'mercury','mg','mini','mitsubishi','morgan','morris','nissan','noble','opel',
	'peugeot','pgo','polestar','pontiac','porsche','princess','renault','rolls-royce',
	'rover','saab','seat','skoda','smart','spectre','ssangyong','subaru','suzuki','talbot',
	'tesla','think','toyota','triumph','tvr','volkswagen','volvo','yugo']

	for i in tqdm(range(len(brands))):
		try:
			listPackage = GetModelUrls(brands[i]).execute()
			if len(listPackage) == 0: raise Exception('list of package null')
		except Exception as erro:
			getLog({
				'erro': erro.args,
				'brand': brands[i],
				'fase': '[fase 1] get urls'
				})
			continue

		for package_i in tqdm(range(len(listPackage))):
			for urlEspc in listPackage[package_i]['urlEspecs']:
				status = False
				sleepTime = 60
				modelCar = listPackage[package_i]['modelCar']
				while not status:
					try:
						tabs = GetModelUrls.getTables(urlEspc)
						titles = GetModelUrls.getTitleTB(urlEspc)
						Tables(
							brands[i], 
							modelCar,
							listPackage[package_i]['fuel'], 
							listPackage[package_i]['cambio'], 
							None, 
							tabs, 
							titles
							).save()
						status =True
					except requests.exceptions.RequestException as erro:
						logErro = {
							'erro': erro.args,
							'brand': brands[i],
							'modelCar': modelCar,
							'url': urlEspc,
							'fase': '[fase 2] get and save tables and titles'
						}
						getLog(logErro)
						print('SLEEP!' + str(sleepTime))
						time.sleep(sleepTime)
						sleepTime += 240
					except ImportError as erroImport:
						logErro = {
							'erro': erroImport.args,
							'brand': brands[i],
							'modelCar': modelCar,
							'url': urlEspc,
							'fase': 'Import Irro'
						}
						getLog(logErro)
				

