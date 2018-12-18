from SPARQLWrapper import *

sparql = SPARQLWrapper("http://localhost:7200/repositories/dummy")

sparql.setHTTPAuth(BASIC)
sparql.setCredentials("admin", "admin")
sparql.setMethod(POST)
sparql.setReturnFormat(JSON)
sparql.setQuery("""
prefix JEMEntitySH: <https://www.JCIBuildingSchema.org/schema/JEMEntitySH#>
SELECT * WHERE
{ ?s a JEMEntitySH:Campus ; ?p ?o . } LIMIT 10
""")

results = sparql.query()
print(results.response.read())