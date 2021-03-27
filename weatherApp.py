#!/bin/python3

import json, sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.recycleview import RecycleView

class WeatherRoot(FloatLayout):
    search_input = ObjectProperty()
    appId = 'abdbe414ad18557599a674e8bd94f8fd'
    #Op3nW34th3r

    def search_location(self):
        search_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.search_input.text}&APPID=" + self.appId
        request = UrlRequest(search_url, self.found_location)
        print("Done ", request)

    def found_location(self, request, data):
        weather_datas = [{'text':"{} ({})".format(data['name'], data['sys']['country'])}]
        print(weather_datas)
        if( len(weather_datas) != 0):
            pass
            #self.search_results.data.insert(0,weather_datas[0])
        self.search_input.text = ""

class HistoryForm(BoxLayout):
    search_results = ObjectProperty()

class RecyclerView(RecycleView):
    def __init__(self, **kwargs):
        super(RecyclerView, self).__init__(**kwargs)

class WeatherApp(App):
    """My App"""

    title = "My Weather App "
    def build(self):
        return WeatherRoot()

if __name__ == '__main__':
    WeatherApp().run()
