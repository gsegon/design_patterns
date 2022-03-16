from DisplayElement import DisplayElement
from Observer import Observer
from WeatherData import WeatherData


class CurrentConditions(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print('Current conditions: ', self.temperature, 'degC and ', self.humidity, ' humidity.')