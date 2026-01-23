class BaseField:
    """Simple descriptor base class for validated config fields."""

    def __init__(self, default=None, required=False):
        self.default = default
        self.required = required
        self.private_name = None

    def __set_name__(self, owner, name):
        # Name mangling for internal storage
        self.private_name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.default)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    def validate(self, value):
        pass
