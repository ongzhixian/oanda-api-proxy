from ariadne import gql, QueryType, make_executable_schema, graphql_sync

# Define type definitions (schema) using SDL

type_defs = gql(
   """
   type Query {
       places: [Place]
       hello: String
   }


   type Place {
       name: String!
       description: String!
       country: String!
       }  
   """
)


# Initialize query

query = QueryType()

# Define resolvers
@query.field("places")
def places(*_):
   return [
       {"name": "Paris", "description": "The city of lights", "country": "France"},
       {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
       {
           "name": "London",
           "description": "The city of big buildings",
           "country": "United Kingdom",
       },
   ]

@query.field("hello")
def hello(*_):
   return "hello world"


# Create executable schema
schema = make_executable_schema(type_defs, query)

# reference: https://blog.logrocket.com/build-graphql-api-python-flask-ariadne/
# reference: https://ariadnegraphql.org/docs/open-tracing
