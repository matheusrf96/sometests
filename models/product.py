
class Product:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.active = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
