import json
from sqlalchemy import TypeDecorator, JSON

class JSONEncodedDict(TypeDecorator):
    """Represents an immutable structure as a json-encoded string."""

    impl = JSON

    def process_bind_param(self, value, dialect):
        if value is not None:
            return value
        return {}

    def process_result_value(self, value, dialect):
        if value is not None:
            return value
        return {}
