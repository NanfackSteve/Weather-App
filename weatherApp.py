#!/bin/python3

import json, sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.recycleview import RecycleView

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    appId = 'abdbe414ad18557599a674e8bd94f8fd'
    #Op3nW34th3r

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/" + "weather?q={}&APPID=" + self.appId
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)
        print("Done ", request)

    def found_location(self, request, data):
        weather_datas = [{'text':"{} ({})".format(data['name'], data['sys']['country'])}]
        print(weather_datas)
        if( len(weather_datas) != 0):
            self.search_results.data.insert(0,weather_datas[0])
        self.search_input.text = ""

class RecyclerView(RecycleView):
    def __init__(self, **kwargs):
        super(RecyclerView, self).__init__(**kwargs)

class WeatherApp(App):
    """My App"""

    title = "My Weather App "
    def build(self):
        return AddLocationForm()



if __name__ == '__main__':
    WeatherApp().run()
