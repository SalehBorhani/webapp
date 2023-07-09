from fastapi import FastAPI , Request , Header
from redis.sentinel import Sentinel
import redis
import uvicorn
from pydantic import BaseModel

api = FastAPI()


class key_value(BaseModel):
    key: str 
    value: str | None = None

@api.get('/')
def welcome():
    return {"Status" : "OK"}

@api.post('/set')
async def post_set(data: key_value):
    server = await redis_connect()
    server.set(data.key , data.value)
    return {"Status" : "OK"}

# first i wrote the set endpoint with GET , and passed key , values as headers
#@api.get('/set')
#async def  redis_set(request : Request):
#    server = await redis_connect()
#    key = request.headers.get('key')
#    value = request.headers.get('value')
#    server.set(key , value)
#    return {"Status" : "OK"}


@api.get('/get/{key}')
# request for passing header
async def  redis_get(request : Request , key: str):
    server = await redis_connect()
    # passing the key as a header
    #key = request.headers.get('key')
    value = server.get(key)
    return {"value": value }

async def redis_connect():
    # can give hostname and ports as env variables to dockerfile as well (ideal way)
    sentinel_instance = Sentinel([("sentinel1" , 26379),("sentinel2" , 26379),("sentinel3" , 26379)])
    host , port = sentinel_instance.discover_master('mymaster')
    try:
        redis_server = redis.Redis(host , port)
    except:
        return {"msg" : "redis unavailable"}
    return redis_server


if __name__ == '__main__':
        uvicorn.run(api, port=80, host='0.0.0.0')
