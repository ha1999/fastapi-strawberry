from fastapi import FastAPI
from app.graphql.index import graphql_app
app = FastAPI()
app.add_route("/graphql", graphql_app)