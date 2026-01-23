from .config import ComponentConfig

class PipelineComponent:
    """
    Base class for all pipeline components.
    Demonstrates:
    - __slots__
    - properties
    - __getattr__ / __setattr__
    - name mangling
    - attribute resolution
    """

    __slots__ = ("config", "__internal_state")

    def __init__(self, name, enabled=True):
        self.config = ComponentConfig(name=name, enabled=enabled)
        self.__internal_state = {}

    # ---------------------------
    # Properties
    # ---------------------------
    @property
    def name(self):
        return self.config.name

    @property
    def is_active(self):
        return self.config.enabled

    # ---------------------------
    # Dynamic attribute handling
    # ---------------------------
    def __getattr__(self, item):
        # Fallback: allow access to config fields as attributes
        if hasattr(self.config, item):
            return getattr(self.config, item)
        raise AttributeError(f"{item} not found")

    def __setattr__(self, key, value):
        # Route config fields to config object
        if key not in self.__slots__ and hasattr(ComponentConfig, key):
            setattr(self.config, key, value)
        else:
            super().__setattr__(key, value)

    # ---------------------------
    # Debug helpers
    # ---------------------------
    def debug_resolution(self):
        return {
            "dict": self.__dict__,
            "class": self.__class__,
            "mro": self.__class__.__mro__,
        }

    # ---------------------------
    # Placeholder for execution
    # ---------------------------
    def run(self):
        raise NotImplementedError("Components must implement run()")

class StringField(BaseField):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")


class BoolField(BaseField):
    def validate(self, value):
        if not isinstance(value, bool):
            raise TypeError("Expected a boolean")

class IntField(BaseField):
    def __init__(self, default=None, required=False, min_value=None, max_value=None):
        super().__init__(default=default, required=required)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected an integer")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value {value} is below minimum {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value {value} is above maximum {self.max_value}")

class ChoiceField(BaseField):
    def __init__(self, choices, default=None, required=False):
        super().__init__(default=default, required=required)
        self.choices = choices

    def validate(self, value):
        if value not in self.choices:
            raise ValueError(f"Value '{value}' must be one of {self.choices}")

class RangeField(BaseField):
    def __init__(self, default=None, required=False, min_value=None, max_value=None):
        super().__init__(default=default, required=required)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Expected a numeric value")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value {value} is below minimum {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value {value} is above maximum {self.max_value}")
