# redis_sentinel
   

# introduction 

* 3 nodes with redis and sentinel , one of them has an api to accept request
* the api gets the master from sentinels whenever it wants to interact with redis 
* redis master , slave and sentinels composes and configs are [here](./redis-composes/)
# node1
```
docker compose -f ~/python_api/api-compose.yml up -d 
docker compose -f ~/master-compose.yml up -d 
docker compose -f ~/sentinels-compose.yml  up -d 
```
# node2
```
docker compose -f ~/slave-2.yml up -d
docker compose -f ~/sentinels-compose.yml  up -d 
```
# node3
```
docker compose  -f ~/slave-1.yml  up -d 
docker compose  -f ~/sentinels-compose.yml  up -d
```

# test
```
curl -X POST -H "Content-Type: application/json" -d '{"key": "ali", "value":"kocholo"}' localhost:8080/set

```
