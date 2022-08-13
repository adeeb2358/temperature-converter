import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from api.mutation import Mutation
from api.query import Query

schema = strawberry.federation.Schema(query=Query, mutation=Mutation)
graphqlApp = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphqlApp, prefix="/graphql")
app.add_websocket_route("/graphql", graphqlApp)
