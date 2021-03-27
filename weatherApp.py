#!/bin/python3

import json, sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import ScreenManager, Screen

class WeatherRoot(Screen, FloatLayout):
    '''Main Layout Launch First'''

    search_input = ObjectProperty()
    appId = 'abdbe414ad18557599a674e8bd94f8fd'
    #Op3nW34th3r

    def search_location(self):
        '''Contact Weather API with API Request'''
        
        #perform url template
        search_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.search_input.text}&APPID=" + self.appId
        request = UrlRequest(search_url, self.found_location)
        print("Done ", request)

    def found_location(self, request, data):
        '''Get API Response'''
        
        weather_datas = [{'text':"{} ({})".format(data['name'], data['sys']['country'])}]
        print(weather_datas)
        if( len(weather_datas) != 0):
            pass
            #self.search_results.data.insert(0,weather_datas[0])
        self.search_input.text = ""
    
    def historyBtn(self):
        '''Launch History Layout'''

        self.search_input.text = ""
        sm.current = "history"

class HistoryForm(Screen, BoxLayout):
    '''Define History Layout'''
    
    search_results = ObjectProperty()

class RecyclerView(RecycleView):
    def __init__(self, **kwargs):
        super(RecyclerView, self).__init__(**kwargs)

#--------------------------- MAIN ------------------------------------------

kv = Builder.load_file("weather.kv")
sm = ScreenManager()
screens = [WeatherRoot(name="main"), HistoryForm(name="history")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "main"

class WeatherApp(App):
    """Define Weather App """

    title = "My Weather App "
    def build(self):
        return sm

if __name__ == '__main__':
    WeatherApp().run()
