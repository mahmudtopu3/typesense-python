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

# json to json line convertion is a must 

with open('languages.jsonl',encoding="utf-8") as jsonl_file:
  print(client.collections['languages'].documents.import_(jsonl_file.read().encode('utf-8'), {'action': 'create'}))
