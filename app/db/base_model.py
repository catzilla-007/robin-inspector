from mongoengine import Document, DateField


class BaseModel(Document):
    created_at = DateField(required=True)
    updated_at = DateField(required=True)
    deleted_at = DateField()

    # TODO: add rules for updating created_at, updated_at, deleted_at