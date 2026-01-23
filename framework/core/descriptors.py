class BaseField:
    """Simple descriptor base class for validated config fields."""
    # default: value returned when instance has no value
    # required: if True, value must be provided
    # private_name: internal storage name for the field and replaced by __set_name__
    def __init__(self, default=None, required=False):
        self.default = default
        self.required = required
        self.private_name = None

    # Pythons calls this method automatically to set the name of the attribute
    # Example: If the descriptor is assigned to 'name' in class ComponentConfig,
    # this method will be called with owner=ComponentConfig and name='name'
    def __set_name__(self, owner, name):
        # Name mangling for internal storage
        self.private_name = f"_{owner.__name__}__{name}"
        
    # Reads the attribute value from the instance
    # If no instance is provided, it means the descriptor is being accessed on the class itself
    # In that case, we return the descriptor itself
    # getattr is used to retrieve the value from the instance's __dict__
    # If the value is not set, we return the default value
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.default)

    # Sets the attribute value on the instance after validation
    # If no instance is provided, it means the descriptor is being accessed on the class itself
    # In that case, we do nothing
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    # Placeholder for validation logic, to be implemented in subclasses
    # here we just pass
    def validate(self, value):
        pass
