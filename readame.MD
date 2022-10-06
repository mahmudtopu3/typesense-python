typesense
https://www.convertjson.com/json-to-jsonlines.htm
https://medium.com/swlh/building-a-search-bar-for-your-gatsbyjs-site-with-typesense-3e277dc33942


docker run -i -p 8108:8108 -v/tmp/typesense-server-data/:/data typesense/typesense:0.15.0 --data-dir /data --api-key=xyz --listen-port 8108 --enable-corss

string	String values
string[]	Array of strings
int32	Integer values up to 2,147,483,647
int32[]	Array of int32
int64	Integer values larger than 2,147,483,647
int64[]	Array of int64
float	Floating point / decimal numbers
float[]	Array of floating point / decimal numbers
bool	true or false
bool[]	Array of booleans
geopoint	Latitude and longitude specified as [lat, lng]
geopoint[]	Arrays of Latitude and longitude specified as [[lat1, lng1], [lat2, lng2]]
string*	Special type that automatically converts values to a string or string[].
auto	Special type that automatically attempts to infer the data type based on the documents added to the collection. See automatic schema detection.