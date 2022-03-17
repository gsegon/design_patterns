from observer.observables.Observable import Observable


class WeatherData(Observable):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None

        self.observers = set()

    def register_observer(self, o):
        self.observers.add(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure





