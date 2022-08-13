import strawberry


# Query and mutation class are needed for graphql service to work.
# As per the requirement , there is no need for query
# this has been added for health check of this api
# In future we can add  graphql queries to this class
@strawberry.type
class Query:
    @strawberry.field
    def healthCheck(self) -> str:
        return "Working!"
