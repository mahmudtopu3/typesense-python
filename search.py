import typesense
from time import time

client = typesense.Client({
  'api_key': 'xyz',
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})

search_parameters = {
  'q'         : 'af',
  'query_by'  : 'name',
#   'filter_by' : 'num_employees:>100',
    'facet_by': 'name'
 
}
res = client.collections['languages'].documents.search(search_parameters)

print(res)
