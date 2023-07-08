
from redis.sentinel import Sentinel
import redis 
# exposed 1001 , 1002 , 1003 for sentinels
sentinel_instance = Sentinel([('localhost' , 1001),('localhost' , 1002),('localhost' , 1003)])

host , port = sentinel_instance.discover_master('mymaster')

# to see the master
print(host , port)

server = redis.Redis(host , port)

server.set("ali" , "asghar")

ali = server.get("ali")
print(ali.decode())