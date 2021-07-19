
class Product:
    name = ''
    description = ''
    active = True

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
