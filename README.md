# Scenario
![Cloud Computing - 1st Competition_2](https://github.com/SalehBorhani/webapp/assets/95637102/a68c06b5-edc7-452c-96ce-5c887adb0e55)

![Cloud Computing - 1st Competition_3](https://github.com/SalehBorhani/webapp/assets/95637102/ff7fb360-ab7d-46d5-af29-c521cac421b1)

# How to test
For send data to database:
```
curl -X POST -H "Content-Type: application/json" -d '{"key": "key1", "value":"value1"}' localhost:8080/set
```
For getting data:
```
curl -H "Content-Type: application/json" -d '{"key": "key1"}' localhost:8080/get
```
