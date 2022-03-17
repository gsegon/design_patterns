from observer.observers.DisplayElement import DisplayElement
from observer.observers.Observer import Observer
from observer.observables.WeatherData import WeatherData


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.pressure = 1025        # hPa
        self.last_pressure = None

        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.last_pressure = self.pressure
        self.pressure = self.weather_data.get_pressure()

        self.display()

    def display(self):
        print('Forecast')

        if self.pressure > self.last_pressure:
            print('Weather will improve!')
        elif self.pressure == self.last_pressure:
            print('Weather will stay the same.')
        elif self.pressure < self.last_pressure:
            print('Weather will worsen! Get an umbrella.')

