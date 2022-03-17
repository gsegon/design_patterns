from observer.observers.Observer import Observer
from observer.observers.DisplayElement import DisplayElement
from observer.observables.WeatherData import WeatherData


class HeatIndexDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.heat_index = None

        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        t = self.weather_data.get_temperature()
        rh = self.weather_data.get_humidity()

        self.heat_index = (
                (16.923 + (0.185212 * t)) +
                (5.37941 * rh) -
                (0.100254 * t * rh) +
                (0.00941695 * (t * t)) +
                (0.00728898 * (rh * rh)) +
                (0.000345372 * (t * t * rh)) -
                (0.000814971 * (t * rh * rh)) +
                (0.0000102102 * (t * t * rh * rh)) -
                (0.000038646 * (t * t * t)) +
                (0.0000291583 * (rh * rh * rh)) +
                (0.00000142721 * (t * t * t * rh)) +
                (0.000000197483 * (t * rh * rh * rh)) -
                (0.0000000218429 * (t * t * t * rh * rh)) +
                (0.000000000843296 * (t * t * rh * rh * rh)) -
                (0.0000000000481975 * (t * t * t * rh * rh * rh)))

        self.display()

    def display(self):
        print('Heat index: ', self.heat_index)
