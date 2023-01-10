from pathlib import Path
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import json

DATA_PATH = "../data/cars.json"

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		
		with open(DATA_PATH, "r") as read_file:
			data = json.load(read_file)
			# for item in data['cars']['carBrand']:
			# 	print(item)
			# print(data['cars']['carBrand'])
			
			# Add a title
			self.setWindowTitle("SearchCar")
			
			# Set layout
			self.setLayout(qtw.QVBoxLayout())
			
			# Create label
			label = qtw.QLabel(data['cars'])
			
			# Change font size of label
			label.setFont(qtg.QFont("Helvetica", 18))
			self.layout().addWidget(label)

			# Create vehicle name
			my_car = qtw.QComboBox(self)
			# Adding car pool
			# my_car.addItem()

			# Exit button
			exit_btn = qtw.QPushButton("Wyjdź", clicked = lambda: sys.exit())
			self.layout().addWidget(exit_btn)

			self.show()

app = qtw.QApplication([])
mw = MainWindow()


#Run the app
app.exec_()