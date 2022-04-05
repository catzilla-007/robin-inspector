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
  "totalFrankys": 3,
  "activeFrankys": 1,
  "version": "1.0.3",
  "serverStartedOn": "time"
}
```

### Get status of Frankys

```
GET /api/v1/frankys
```

Response

```json
[
  {
    "id": "uuid",
    "name": "franky-1",
    "state": "active",
    "connection": "connected",
    "startedOn": "time",
    "stoppedOn": null,
    "ip": "192.168.1.3",
    "port": 80
  },
  {
    "id": "uuid",
    "name": "franky-2",
    "state": "inactive",
    "connection": "disconnected",
    "startedOn": null,
    "stoppedOn": null,
    "ip": "192.168.1.2",
    "port": 80
  }
]
```
### Get status of a specific Franky

```
GET /api/v1/frankys/<uuid>
```

Response

```json
{
  "id": "uuid",
  "name": "franky-3",
  "state": "active",
  "connection": "reachable",
  "startedOn": "time",
  "stoppedOn": null,
  "ip": "192.168.1.4",
  "port": 80
}
```

### Create a Franky

```
POST /api/v1/frankys
```

Body

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
  "state": "inactive",
  "connection": "reachable",
  "startedOn": null,
  "stoppedOn": null,
  "ip": "192.168.10.1",
  "port": 80
}
```

### Delete a Franky

```
DELETE /api/v1/frankys/<uuid>
```

Response 

```json
{
  "id": "uuid"
}
```

### Start a Franky

```
POST /api/v1/frankys/<uuid>/start
```

Response

```json
{
  "state": "active",
  "connection": "connected",
  "startedOn": "time"
}
```

### Stop a Franky

```
POST /api/v1/frankys/<uuid>/stop
```

Response

```json
{
  "state": "inactive",
  "connection": "disconnected",
  "startedOn": "time",
  "stoppedOn": "time"
}
```
