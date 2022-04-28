from controller.GetUrls import GetModelUrls
from model.Tables import Tables

if __name__ == '__main__':

	brand = 'abarth'

	listPackage = GetModelUrls(brand).execute()
	for package in listPackage:
		for urlEspc in package['urlEspecs']:
			modelCar = package['modelCar']
			tabs = GetModelUrls.getTables(urlEspc)
			titles = GetModelUrls.getTitleTB(urlEspc)
			Tables(brand, modelCar,package['fuel'], package['cambio'], None, tabs, titles).save()
			

