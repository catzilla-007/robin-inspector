# Robin Inspector

A FastAPI server deployed in raspberry pi that collects information from sensors used in hydrophonics.

Sensors are connected to an arduino microcontroller and a serial connection to the raspberry pi will be used
for getting data in the sensors.

### Available Endpoints

```
GET /api/v1/water-level
```

Response
```json
{
  "timestamp": "2022-03-22 15:33:32",
  "value": "50%",
  "type": "water-level"
}
```