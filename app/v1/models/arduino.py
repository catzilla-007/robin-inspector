from pydantic import BaseModel


class ArduinoRequest(BaseModel):
    name: str
    ip: str
    port: int = 80
