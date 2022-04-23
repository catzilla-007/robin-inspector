from mongoengine import StringField, IntField

from app.db.base_model import BaseModel


class Arduino(BaseModel):
    name = StringField(required=True)
    ip = StringField(required=True)
    port = IntField(default=80)
    state = StringField(default="inactive")
