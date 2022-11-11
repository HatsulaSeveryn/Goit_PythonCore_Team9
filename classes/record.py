from datetime import datetime
from classes.name import Name
from classes.phone import Phone
from classes.birthday import Birthday


class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address: str = None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = ''

    def __str__(self):

        if self.birthday:
            return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}, birthday: {str(self.birthday)}'
        else:
            return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
