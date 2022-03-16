from WeatherData import WeatherData
from CurrentConditions import CurrentConditions

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions = CurrentConditions(weather_data)

    weather_data.set_measurements(10, 30, 20)
    weather_data.set_measurements(11.3, 28.4, 23.1)
    weather_data.set_measurements(10, 30, 20)


