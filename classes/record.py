
from classes.name import Name
from classes.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ''
        self.address = ''
        self.email = ''

    def __str__(self):
        return f'Name {self.name.value} - tel:  {", ".join([phone.value for phone in self.phones])}; birthday: {str(self.birthday)}; email: {str(self.email)}; address: {self.address}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.phones.append(Phone(new_phone))
