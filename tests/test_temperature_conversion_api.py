import datetime

import pytest as pytest
import strawberry

from api.mutation import Mutation
from api.query import Query


@pytest.fixture
def mutation():
    return "mutation convert ($temperature:Float!,$unitToConvert:Unit!){ \
            convertTemperature(inputTemperature:$temperature, unitToConvert: $unitToConvert) { \
                unit \
                value \
                convertedAt \
                }\
            } "


@pytest.fixture
def query():
    return "query healthCheck{ healthCheck }"


@pytest.fixture
def schema():
    return strawberry.Schema(query=Query, mutation=Mutation)


def assertNoErrors(result):
    assert result.errors is None
    assert result.data is not None


async def executeQuery(schema, query, queryParams=None):
    return await schema.execute(query=query, variable_values=queryParams)


def assertTemperatureValues(result, value, unit, requestStartTime):
    temperature = result.data['convertTemperature']
    assert temperature['value'] == value
    assert temperature['unit'] == unit
    convertedTime = datetime.datetime.strptime(temperature['convertedAt'], '%Y-%m-%dT%H:%M:%S.%f')
    assert requestStartTime < convertedTime < datetime.datetime.now()


def createInputTemperature(value, unit):
    inputTemperature = {'temperature': value, 'unitToConvert': unit}
    return inputTemperature


@pytest.mark.asyncio
async def test_succeeds_when_converting_celsius_to_fahrenheit(schema, mutation):
    requestStartTime = datetime.datetime.now()
    inputTemperature = createInputTemperature(12345.6, 'FAHRENHEIT')
    result = await executeQuery(schema, mutation, inputTemperature)
    assertNoErrors(result)
    assertTemperatureValues(result, 22254.08, 'FAHRENHEIT', requestStartTime)
    pass


@pytest.mark.asyncio
async def test_succeeds_when_converting_fahrenheit_to_celsius(schema, mutation):
    requestStartTime = datetime.datetime.now()
    inputTemperature = createInputTemperature(22254.08, 'DEGREE_CELSIUS')
    result = await executeQuery(schema, mutation, inputTemperature)
    assertNoErrors(result)
    assertTemperatureValues(result, 12345.6, 'DEGREE_CELSIUS', requestStartTime)
    pass


@pytest.mark.asyncio
async def test_fails_when_unit_is_invalid(schema, mutation):
    inputTemperature = createInputTemperature(22254.08, 'INVALID_UNIT_TYPE')
    result = await executeQuery(schema, mutation, inputTemperature, )
    assert len(result.errors) == 1
    assert result.errors[
               0].message == "Variable '$unitToConvert' got invalid value 'INVALID_UNIT_TYPE'; " \
                             "Value 'INVALID_UNIT_TYPE' does not exist in 'Unit' enum."
    pass


@pytest.mark.asyncio
async def test_fails_when_temperature_value_is_invalid(schema, mutation):
    inputTemperature = createInputTemperature('INVALID_VALUE', 'DEGREE_CELSIUS')
    result = await executeQuery(schema, mutation, inputTemperature)
    assert len(result.errors) == 1
    assert result.errors[0].message == "Variable '$temperature' got invalid value 'INVALID_VALUE'; " \
                                       "Float cannot represent non numeric value: 'INVALID_VALUE'"
    pass


@pytest.mark.asyncio
async def test_succeeds_when_health_check_api_is_executed(schema, query):
    result = await executeQuery(schema, query)
    assertNoErrors(result)
    assert result.data['healthCheck'] == 'Working!'
    pass
