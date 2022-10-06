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


# Create a collection

while not client.operations.is_healthy():
  print("cluster is unhealthy, retrying...")
  time.sleep(1)
#print("cluster is healthy")


schema = {
  'name': 'companies',
  'fields': [
    {
      'name'  :  'company_name',
      'type'  :  'string'
    },
    {
      'name'  :  'num_employees',
      'type'  :  'int32'
    },
    {
      'name'  :  'country',
      'type'  :  'string',
      'facet' :  True
    }
  ],
  'default_sorting_field': 'num_employees'
}

    # "code": "aa",
    # "name": "Afar",
    # "native": "Afar"
schema2 = {
  'name': 'languages',
  'fields': [
    {
      'name'  :  'code',
      'type'  :  'string'
    },
    {
      'name'  :  'native',
      'type'  :  'string'
    },
    {
      'name'  :  'name',
      'type'  :  'string',
      'facet' :  True
    }
  ],

}



#client.collections.create(schema2)
document = {
  'id': '124',
  'company_name': 'Stark Industries',
  'num_employees': 5215,
  'country': 'USA'
}

#client.collections['companies'].documents.create(document)


#print(client.collections['languages'].retrieve())

#print(client.collections['languages'].documents['50'].retrieve())


print(client.collections['languages'].synonyms.retrieve())