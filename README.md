## 1. Memory alert

To run script with 75% memory threshold alert:

```
bash memory_check.sh 75 https://some-endpoint.com/memory/
```

## 2. Key-value app

-------
This project ties together Flask and Redis. 
A simple project with functions such as create, update, get and delete.
Also here is bash script which controls the memory usage and generates alarm by sending http request to API.

-------
### QUICKSTART

Clone the repository, cd into it and run

```
docker-compose up -d
```

### URLs

* POST `/key/` - store value
* POST `/key/<key>/` - get value
* PUT `/key/<key>/` - update value
* DELETE `/key/<key>/` - delete value

### Basic usage

Create value:
```
curl -d '{"key": "my-key", "value": "my-value"}' -H "Content-Type: application/json" -X POST http://localhost:8080/key/
```

Get value:
```
curl localhost:8080/key/my-key/
```

Update value:
```
curl -d '{"value": "new-value"}' -H "Content-Type: application/json" -X PUT localhost:8080/key/my-key/
```

Delete value:
```
curl -X DELETE http://localhost:8080/key/my-key/
```

