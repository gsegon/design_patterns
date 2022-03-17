from observer.observers.DisplayElement import DisplayElement
from observer.observers.Observer import Observer
from observer.observables.WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):

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
        print('Current conditions: ', self.temperature, 'degF and ', self.humidity, ' humidity.')