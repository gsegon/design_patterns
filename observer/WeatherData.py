from Subject import Subject


class WeatherData(Subject):

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
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

