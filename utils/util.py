import json

DATA_PATH = "./data/cars.json"

def openFile(path=DATA_PATH):
	with open(DATA_PATH, "r") as read_file:
			data = json.load(read_file)
			return data


def getBrandData(data=DATA_PATH):
	# for label in data['cars']:
	# 	for key, value in label.items():
	# 		if key == 'carBrand':
	# 			carBrand.append(value)
	print(" s")

def getBrandName(data=DATA_PATH):
	carBrand = []
	file = openFile()
	for label in file['cars']:
				for key, value in label.items():
					if key == 'carBrand':
						carBrand.append(value)
	print(f'This is it -> {carBrand}')
	return carBrand
