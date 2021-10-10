from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.sensors import Sensors


class Response(BaseModel):
    timestamp: Optional[datetime] = datetime.now()
    value = ''
    type: Sensors
