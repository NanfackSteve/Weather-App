import json
import sys
from urllib.error import HTTPError
from PyQt5 import QtWidgets
from urllib.request import urlopen
from interface import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def search_location():
    header = "http://api.openweathermap.org/data/2.5/weather?q="
    appID = "abdbe414ad18557599a674e8bd94f8fd"
    location = ui.lineEdit.text()

    if ui.lineEdit.text() == "":
        print("Error")
    else:
        url_request = header + f"{location}&APPID=" + appID
        try:
            response = urlopen(url_request)
            json_data = json.loads(response.read())
            # print("\n", json_data) # print json Data
            ui.country.setText(json_data["sys"]["country"])
            ui.city.setText(json_data["name"])
            ui.main.setText(json_data["weather"][0]["main"])
            ui.description.setText(json_data["weather"][0]["description"])

            t_celcius = float(json_data["main"]["feels_like"]) - 273.15
            t_celcius = float("{:.2f}".format(t_celcius))
            ui.temperature.setText(str(t_celcius) + " °C")
            ui.pressure.setText(str(json_data["main"]["pressure"]) + " hPa")
            ui.humidity.setText(str(json_data["main"]["humidity"]) + "%")
            ui.cloud.setText(str(json_data["clouds"]["all"]) + "%")

        except HTTPError:
            print("Invalid Location")

    ui.lineEdit.setText("")


ui.pushButton.clicked.connect(search_location)

sys.exit(app.exec_())
