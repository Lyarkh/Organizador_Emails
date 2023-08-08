class Config:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                value = self.new_instance_class(value)
            setattr(self, key, value)

    @classmethod
    def new_instance_class(cls, data):
        return cls(data)
