import datetime
from enum import Enum

import strawberry


@strawberry.enum
class Unit(Enum):
    DEGREE_CELSIUS = "DEGREE_CELSIUS"
    FAHRENHEIT = "FAHRENHEIT"


# schema for temperature data representation in the api contract
@strawberry.federation.type
class Temperature:
    value: float
    unit: Unit
    convertedAt: datetime.datetime
