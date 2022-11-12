from collections import UserDict
from datetime import datetime
import pickle
from classes.record import Record
from classes.name import Name


class AddressBook(UserDict):

    def input_error(func):

        def inner(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Wrong name"
            except TypeError:
                return "Wrong command"
            except IndexError:
                return "Enter name and phone"
            except ValueError as e:
                return e.args[0]
            except Exception as e:
                return e.args

        return inner

    def iterator(self):
        for record in self.data.values():
            yield record

    def add_address(self, name, addr):

        if not name in self.data:
            self.add_contact(name)

        self.data[name].address = addr

    def add_birthday(self, name, birthday):

        if not name in self.data:
            self.add_contact(name)

        self.data[name].birthday = birthday

    def add_contact(self, name):

        if not name in self.data:
            new_record = Record(name)
            self.data[new_record.name.value] = new_record
            print(f'For {name} add contact at AdressBook')

        else:
            return f'Contact with this name exist. Try other name or other command'

    def add_email(self, name, email):

        if not name in self.data:
            self.add_contact(name)

        self.data[name].email = email

    def add_phone(self, name, phone):

        if not name in self.data:
            self.add_contact(name)

        self.data[name].add_phone(phone)

    def remove_contact(self, name):

        try:
            self.data.__delitem__(name)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_phone(self, name, phone=None):

        if phone:

            try:
                self.data[name].delite_phone(phone)

            except KeyError:
                raise ValueError(f'Contact {name} has not been found')

    def change_phone(self, name, old_phone, new_phone):
        """Change old number phone  for name which is in Contacts to new phone"""

        try:
            self.data[name].edit_phone(old_phone, new_phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')


#        if self.data[name].edit_phone(old_phone, new_phone):
#            return f'For {name} has changed phone number {old_phone} at: {new_phone}'

#        return f' {name} has not phone number {old_phone} in contact'

#    return f'Contact {name_contact} not in phone book'


    def show_all_contact(self, number_on_page=None):
        quantity_records_on_page = 3
        stock = self.iterator()
        page = 1
        while True:
            try:
                for _ in range(quantity_records_on_page):
                    print(next(stock))
                print(f"Page:   {page}")
                page += 1
            except StopIteration:
                print("it's end.No contacts in book")
                break
