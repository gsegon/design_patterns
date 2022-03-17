from observer.observables.WeatherData import WeatherData
from observer.observers.CurrentConditionsDisplay import CurrentConditionsDisplay
from observer.observers.StatisticsDisplay import StatisticsDisplay
from observer.observers.ForecastDisplay import ForecastDisplay

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forcast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(2, 30, 1000)
    weather_data.set_measurements(6, 28.4, 1100)
    weather_data.set_measurements(4, 30, 900)
    weather_data.set_measurements(4, 30, 950)
    weather_data.set_measurements(12, 30, 100)
    weather_data.set_measurements(12, 30, 110)


