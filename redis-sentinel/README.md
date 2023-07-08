# redis_sentinel
   

# introduction 

* 3 nodes with redis and sentinel , one of them has an api to accept request
* the api gets the master from sentinels whenever it wants to interact with redis 
* the files will be added
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
NOT INCLUDED YET
```
