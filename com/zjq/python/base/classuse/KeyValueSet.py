class KeyValueSet:
    def __init__(self) -> None:
        self.dict = {}

    def set(self, key, value):
        self.dict[key] = value

    def get(self, key):
        return self.dict.get(key)

    def keys(self):
        return self.dict.keys()