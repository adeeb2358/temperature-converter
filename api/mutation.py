import strawberry

from api.resolver import Resolver
from api.schema import Temperature


@strawberry.type
class Mutation:
    # this is the mutation for converting temperature from degree to celsius and vice versa
    convertTemperature: Temperature = strawberry.mutation(resolver=Resolver().convertTemperature)
