from .descriptors import StringField, BoolField

class ComponentConfig:
    """Configuration object using descriptors for validation."""

    name = StringField(required=True)
    enabled = BoolField(default=True)

    def __init__(self, name, enabled=True):
        self.name = name
        self.enabled = enabled
