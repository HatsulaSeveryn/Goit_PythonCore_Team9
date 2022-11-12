from collections import UserDict
from datetime import datetime
import pickle
from classes.record import Record
from classes.name import Name
from classes.birthday import Birthday
from classes.email import Email


class AddressBook(UserDict):

    def __init__(self, filename='adress_book.txt'):
        super().__init__()
        self.filename = filename
        self.read_adress_book_from_file()

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

    def write_adress_book_file(self):
        with open('adress_book.txt', 'wb') as file:
            pickle.dump(self.data, file)

    def read_adress_book_from_file(self):
        try:
            with open('adress_book.txt', 'rb') as file:
                self.data = pickle.load(file)
                return self.data
        except FileNotFoundError:
            pass

    def add_address(self, name, addr):

        if not name in self.data:
            self.add_contact(name)

        self.data[name].address = addr
        return True

    def add_birthday(self, name, birthday):

        if not name in self.data:
            self.add_contact(name)
        try:

            self.data[name].birthday = Birthday(birthday)
        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')
        return True

    def add_contact(self, name):

        if not name in self.data:
            new_record = Record(name)
            self.data[new_record.name.value] = new_record
            print(f'For {name} add contact at AdressBook')

        else:
            return f'Contact with this name exist. Try other name or other command'
        return True

    def add_email(self, name, email):

        if not name in self.data:
            self.add_contact(name)

        try:

            self.data[name].email = Email(email)

        except ValueError:
            raise "Mistake in email, example: my_email@pyton.com"
        return True

    def add_phone(self, name, phone):

        if not name in self.data:
            self.add_contact(name)

        try:

            self.data[name].add_phone(phone)
        except ValueError:
            raise "Not correct format for phone"
        return True

    def remove_address(self, name):
        try:
            self.data[name].address = ''
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def remove_birthday(self, name):
        try:
            self.data[name].birthday = ''
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def remove_contact(self, name):

        try:
            self.data.__delitem__(name)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def remove_email(self, name):
        try:
            self.data[name].email = ''
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def remove_phone(self, name, phone=None):

        if phone:

            try:
                self.data[name].delite_phone(phone)

            except KeyError:
                raise ValueError(f'Contact {name} has not been found')
            return True

    def change_address(self, name, address):
        """Change old address  for name which is in Contacts to new address. 
        If contact has not old address - address will be add"""

        try:
            self.data[name].address = address
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def change_email(self, name, email):
        """Change old mail  for name which is in Contacts to new mail. 
        If contact has not old mail - mail will be add"""

        try:
            self.data[name].email = Email(email)
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Mistake in email')
        return True

    def change_phone(self, name, old_phone, new_phone):
        """Change old number phone  for name which is in Contacts to new phone"""

        try:
            self.data[name].edit_phone(old_phone, new_phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        return True

    def change_birthday(self, name, birthday):
        """Change old birthday  for name which is in Contacts to new """

        try:
            self.data[name].birthday = Birthday(birthday)
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')
        return True

    def save_to_file(self, file_name):
        self.write_adress_book_file()
        return 'Data has been saved'

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

    def quit_func(self):
        self.write_adress_book_file()
        return 'Good bye!'
