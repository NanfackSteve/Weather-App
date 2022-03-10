import json
import sys
from urllib.error import HTTPError
from PyQt5 import QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from urllib.request import urlopen
from lib.interface import Ui_MainWindow
from lib.warning import Ui_Dialog as WarningDialog

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

# centrer la fenetre
qr = MainWindow.frameGeometry()
qr.moveCenter(QtWidgets.QDesktopWidget().availableGeometry().center())
MainWindow.move(qr.left(), 100)
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# creation du Warning
Warning = QtWidgets.QDialog()
uiWarning = WarningDialog()
uiWarning.setupUi(Warning)

MainWindow.show()


def search_location():
    """Give the Weather of Specific location"""

    header = "http://api.openweathermap.org/data/2.5/weather?q="
    appID = "abdbe414ad18557599a674e8bd94f8fd"
    location = ui.lineEdit.text()

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
        Warning.show()

    ui.lineEdit.clear()
    ui.lineEdit.setDisabled(True)
    ui.lineEdit.setDisabled(False)


# Le champ de Text n'accepte que des [a-zAZ]
ui.lineEdit.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
ui.lineEdit.returnPressed.connect(search_location)
ui.pushButton.clicked.connect(search_location)

sys.exit(app.exec_())
