from mongoengine import Document, DateTimeField
from datetime import datetime


class BaseModel(Document):
    meta = {'abstract': True}

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())
    deleted_at = DateTimeField()
