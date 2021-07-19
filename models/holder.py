
class Holder:
    name = ''
    document = ''
    email = ''
    phone = ''

    def __init__(self, name, document, email, phone):
        self.name = name
        self.document = document
        self.email = email
        self.phone = phone

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
