import datetime

import pytemperature

from api.schema import Unit, Temperature


# the class which is responsible for the actual conversion function
class Resolver:
    def __init__(self):
        self.converter = pytemperature
        pass

    async def convertTemperature(self, inputTemperature: float, unitToConvert: Unit) -> Temperature:
        if unitToConvert is Unit.FAHRENHEIT:
            return self.convertDegreeCelsiusToFahrenheit(inputTemperature)
        else:
            return self.convertFahrenheitToDegreeCelsius(inputTemperature)

    def convertDegreeCelsiusToFahrenheit(self, inputTemperature: float):
        fahrenheitValue = self.converter.c2f(inputTemperature)
        temperature = Temperature(fahrenheitValue, Unit.FAHRENHEIT, datetime.datetime.now())
        return temperature

    def convertFahrenheitToDegreeCelsius(self, inputTemperature: float):
        degreeCelsiusValue = self.converter.f2c(inputTemperature)
        temperature = Temperature(degreeCelsiusValue, Unit.DEGREE_CELSIUS, datetime.datetime.now())
        return temperature


