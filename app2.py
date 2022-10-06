import typesense

client = typesense.Client({
  'nodes': [{
    'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '8108',      # For Typesense Cloud use 443
    'protocol': 'http'   # For Typesense Cloud use https
  }],
  'api_key': 'xyz',
  'connection_timeout_seconds': 2
})

books_schema = {
  'name': 'books',
  'fields': [
    {'name': 'title', 'type': 'string' },
    {'name': 'authors', 'type': 'string[]', 'facet': True },

    {'name': 'publication_year', 'type': 'int32', 'facet': True },
    {'name': 'ratings_count', 'type': 'int32' },
    {'name': 'average_rating', 'type': 'float' }
  ],
  'default_sorting_field': 'ratings_count'
}

#client.collections.create(books_schema)

# insert book collection
#with open('books.jsonl',encoding="utf-8") as jsonl_file:
  #client.collections['books'].documents.import_(jsonl_file.read().encode('utf-8'))

#data about collection books
#print(client.collections['books'].retrieve())


search_parameters1 = {
  'q'         : 'harry potter',
  'query_by'  : 'title',
  'sort_by'   : 'ratings_count:desc',
  'page': 1,
  'include_fields': 'title,publication_year',
  'per_page': 5
}

search_parameters2 = {
  'q'         : 'harry potter',
  'query_by'  : 'title',
  'filter_by' : 'publication_year:<1998',
  'sort_by'   : 'publication_year:desc'
}
search_parameters3 = {
  'q'         : 'experyment',
  'query_by'  : 'title',
  'facet_by'  : 'authors',
  'sort_by'   : 'average_rating:desc'
}
res = client.collections['books'].documents.search(search_parameters1)
print(res)

#django  after getting all id make it a list, then in django return qs__in(list)

# http://0.0.0.0:8108/health  headers X-TYPESENSE-API-KEY xyz  Content-Type  application/json

"""
var myHeaders = new Headers();
myHeaders.append("X-TYPESENSE-API-KEY", "xyz");
myHeaders.append("Content-Type", "application/json");

var formdata = new FormData();

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("http://0.0.0.0:8108/health", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
"""