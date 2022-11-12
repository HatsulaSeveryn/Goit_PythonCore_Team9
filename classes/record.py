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

        if address:
            self.address = address
        else:
            self.address = ''

        if email:
            self.email = email
        else:
            self.email = ''

    def __str__(self):

        #        if self.birthday:
        #            return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}, birthday: {str(self.birthday)}, email: {self.email}, address: {self.address}'
        #        else:
        return f'Name {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}, birthday: {str(self.birthday)}, email: {self.email}, address: {self.address}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delite_phone(self, del_phone):
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
#                edit_done=True
                return True
        print(f'Phone {old_phone} not found in data')
        return False
