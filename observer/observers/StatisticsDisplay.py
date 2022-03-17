from observer.observers.Observer import Observer
from observer.observers.DisplayElement import DisplayElement
from observer.observables.WeatherData import WeatherData


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):

        self.mean_temperature = None
        self.max_temperature = None
        self.min_temperature = None
        self.count = 0

        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):

        if self.count == 0:
            self.mean_temperature = temperature
            self.max_temperature = temperature
            self.min_temperature = temperature
        else:
            self.mean_temperature += (temperature-self.mean_temperature)/(self.count+1)
            self.min_temperature = min(self.min_temperature, temperature)
            self.max_temperature = max(self.max_temperature, temperature)

        self.count += 1

        self.display()

    def display(self):
        print('Statictics: ')
        print('Tavg: ', self.mean_temperature, '\t(min: ', self.min_temperature, ', max: ', self.max_temperature, ' )')



