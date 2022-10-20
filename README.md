# Robin Inspector

A FastAPI server deployed in raspberry pi that collects information from sensors used in hydrophonics.

Sensors are connected to an arduino microcontroller and a REST API to the raspberry pi will be used
for getting data in the sensors.

Robin Inspector will act as a manager and collector of information that all the deployed Franky bot has. 
Historical information of sensors' value will be saved in a MongoDB database.

## API

### Get general status

```
GET /api/v1/status
```

Response

```json
{
  "arduino": {
    "count": 3,
    "active": 2
  },
  "version": "1.0.3",
  "startedOn": "timestamp"
}
```

### Get status of Arduinos

```
GET /api/v1/arduinos
```

Response

```json
[
  {
    "id": "uuid",
    "name": "franky-1",
    "status": "active",
    "startedOn": "timestamp",
    "stoppedOn": null,
    "ip": "192.168.1.3",
    "port": 80
  },
  {
    "id": "uuid",
    "name": "franky-2",
    "status": "inactive",
    "startedOn": null,
    "stoppedOn": null,
    "ip": "192.168.1.2",
    "port": 80
  }
]
```
### Get status of a specific Arduino

```
GET /api/v1/arduinos/<uuid>
```

Response

```json
{
  "id": "uuid",
  "name": "franky-3",
  "status": "active",
  "startedOn": "timestamp",
  "stoppedOn": null,
  "ip": "192.168.1.4",
  "port": 80
}
```

### Create an Arduino

```
POST /api/v1/arduinos
```

Request

```json
{
  "name": "Franky-4",
  "ip": "192.168.10.1",
  "port": 80
}
```

Response

```json
{
  "id": "uuid",
  "name": "Franky-4",
  "status": "inactive",
  "ip": "192.168.10.1",
  "port": 80
}
```

### Delete an Arduino

```
DELETE /api/v1/arduinos/<uuid>
```

Response 

```json
{
  "id": "uuid"
}
```

### Start sensor collection of an Arduino

This will send a message to a message broker for starting arduino collection

```
POST /api/v1/arduinos/<uuid>/start
```

Response

```json
{
  "status": "active",
  "connection": "connected",
  "startedOn": "timestamp"
}
```

### Stop sensor collection of an Arduino

This will send a message to a message broker for stopping arduino collection

```
POST /api/v1/arduino/<uuid>/stop
```

Response

```json
{
  "status": "inactive",
  "startedOn": "timestamp",
  "stoppedOn": "timestamp"
}
```
