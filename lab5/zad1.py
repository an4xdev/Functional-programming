# Z1.
class JsonRepresentable:
    def to_json(self):
        return '{\n    "name": "'+self.name+'",\n    "email": "'+self.email+'"\n}'


class XmlRepresentable:
    def to_xml(self):
        return f"<Contact>\n    <name>{self.name}</name>\n    <email>{self.email}</email>\n</Contact>"

# Klasa Contact, która dziedziczy z obu klas bazowych


class Contact(JsonRepresentable, XmlRepresentable):
    def __init__(self, name, email):
        self.name = name
        self.email = email


contact = Contact("Michał", "mz87604@stud.uph.edu.pl")
print(contact.to_json())
print(contact.to_xml())
