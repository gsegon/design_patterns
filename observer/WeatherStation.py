from observer.observables.WeatherData import WeatherData
from observer.observers.CurrentConditionsDisplay import CurrentConditionsDisplay
from observer.observers.StatisticsDisplay import StatisticsDisplay
from observer.observers.ForecastDisplay import ForecastDisplay
from observer.observers.HeatIndexDisplay import HeatIndexDisplay

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    heat_index_display = HeatIndexDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)     # temperature [degF], relative humidity [%], pressure [inHg]
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


