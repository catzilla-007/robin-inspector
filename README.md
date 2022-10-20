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
    "connected": 2,
    "active": 1
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
    "connection": "connected",
    "startedOn": "timestamp",
    "stoppedOn": null,
    "host": "192.168.1.3",
    "port": 80
  },
  {
    "id": "uuid",
    "name": "franky-2",
    "status": "inactive",
    "connection": "disconnected",
    "startedOn": null,
    "stoppedOn": null,
    "host": "192.168.1.2",
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
  "connection": "connected",
  "startedOn": "timestamp",
  "stoppedOn": null,
  "host": "192.168.1.4",
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
  "host": "192.168.10.1",
  "port": 80
}
```

Response

```json
{
  "id": "uuid",
  "name": "Franky-4",
  "status": "inactive",
  "connection": "connected",
  "host": "192.168.10.1",
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


## DB Schemas


#### BaseModel

all DB collections will extend base model

```json
{
  "id": "uuid",
  "createdAt": "timestamp",
  "updatedAt": "timestamp",
  "deletedAt": "timestamp"
}
```

#### Arduinos

Stores information of arduinos connected to the hydrophonics and robin-inspector.
This is also used to start/stop collection of information

```json
{
  "name": "string",
  "host": "ip",
  "port": "port",
  "status": "active | inactive",
  "connection": "connected | disconnected"
}
```

#### Plants

Stores information of the plants planted.

```json
{
  "name": "random name?",
  "plant": "type of plant planted",
  "plantedOn": "when it is planted",
  "substrate": "what material is used for planting",
  "harvestedOn": "when it is harvested",
  "arduino": "ref#arduinos: what arduino is used to record this"
}
```

#### Sensor Data

```json
{
  "arduino": "ref#arduinos",
  "batch": "ref#batch",
  "sensors": [
    "temperature",
    "waterTemperature",
    "ph",
    "tds",
    "waterLevel",
    "light",
    "humidity"
  ],
  "temperature": {
    "value": "number",
    "unit": "celcius"
  },
  "waterTemperature": {
    "value": "number",
    "unit": "celcius"
  },
  "ph": {
    "value": "number",
    "unit": "ph"
  },
  "tds": {
    "value": "number",
    "unit": "ppm"
  },
  "waterLevel": {
    "value": "low | normal | high",
    "unit": ""
  },
  "light": {
    "value": "number",
    "unit": "lumens"
  },
  "humidity": {
    "value": "number",
    "unit": "%"
  }
}
```

future sensors
- gpm - gallons per minute
- ec - electrical current - how much salt


## Data Parameters

status
- `active`
  - collection is enabled
- `inactive`
  - collection is disabled

connection
- `connected`
  - device is reachable from the server
- `disconnected`
  - device is not reachable from the server

  