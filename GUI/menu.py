import sys, os, json
from pathlib import Path
from src import source
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

DATA_PATH = "./data/cars.json"

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.setFixedSize(640, 480)

		with open(DATA_PATH, "r") as read_file:
			data = json.load(read_file)
			print(os.getcwd())
			# for key, item in data.items():
			# 	for name in item:
			# 		print(name)
			# 	print(key)
			# for key, value in data.items():
			# 	print(value)
			# print(data['cars'])
			# print(data['cars'][0])
			# for listLength in data['cars']
			# listLength = len(data['cars']) - 1
			carList = []
			carBrand = []
			# for index in len(data['cars']):
			# 	print(data['cars'][index].items())
			# print(data['cars'])
			# print(data['cars'][0]['carBrand'])
			for label in data['cars']:
				for key, value in label.items():
					if key == 'carBrand':
						carBrand.append(value)
					print(f'{key} -> {value}')
			print(carBrand)
			# for index in data['cars']:
			# 	# print(index)
			# 	for key, value in index.items():
			# 		carBrand.append(index)
			# 		print(f"{key} -> {value} TU JESTEM")
			# print(f"{carBrand} -> LISTA MAREK SAMOCHODÓW")
			# for key, value in data['cars'][listLength].items():
			# 	for car in value:
			# 		print(value)
			# 		if key == "carModel":
			# 			carList.append(car)
			
			# print(f"Marka Twojego wybranego samochodu to {carList}Lista Twoich samochodów to: {carList}")
			# carModels = [(key, value) for key, values in data.items() for value in values]
			# for model in carModels:
			# 	print(model)

			# Add a title
			self.setWindowTitle("SearchCar")
			
			# Set layout
			self.setLayout(qtw.QVBoxLayout())
			
			# Create label
			label = qtw.QLabel('chuj')
			
			# Change font size of label
			label.setFont(qtg.QFont("Helvetica", 18))
			self.layout().addWidget(label)

			# Show car brand
			my_car = qtw.QComboBox(self)
			# Show brand models
			my_carList = qtw.QComboBox(self)
			# Move carList ComboBox
			my_carList.move(105, 0 )
			# Adding car pool
			my_car.addItems(carBrand)
			print(source.getBrandData())
			# Adding action to combo box, if given carBrand is chosen my_carList lists cars of specified carBrand
			# my_car.activated()

			# Exit button
			exit_btn = qtw.QPushButton("Wyjdź", clicked = lambda: sys.exit())
			self.layout().addWidget(exit_btn)

			self.show()

app = qtw.QApplication([])
mw = MainWindow()


#Run the app
app.exec_()