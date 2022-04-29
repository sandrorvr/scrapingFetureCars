from controller.GetUrls import GetModelUrls
from model.Tables import Tables
from tqdm import tqdm
import time

if __name__ == '__main__':

	brands = ['abarth','aiways','alfa-romeo','alpine','asia-motors',
	'aston-martin','audi','austin','autobianchi','bentley','bmw','bugatti',
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
		listPackage = GetModelUrls(brands[i]).execute()
		for package in listPackage:
			timeSleep = 20
			for urlEspc in package['urlEspecs']:
				modelCar = package['modelCar']
				tabs = GetModelUrls.getTables(urlEspc)
				titles = GetModelUrls.getTitleTB(urlEspc)
				Tables(brands[i], modelCar,package['fuel'], package['cambio'], None, tabs, titles).save()
			timeSleep += 1
			time.sleep(timeSleep)
				

