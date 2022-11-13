from collections import UserDict
import pickle
from classes.birthday import Birthday
from classes.email import Email
from classes.record import Record


class AddressBook(UserDict):

    def __init__(self, filename='adress_book.txt'):
        super().__init__()
        self.filename = filename
        self.read_adress_book_from_file()

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
        try:
            self.data[name].address = addr
            print(f'For {name} add address {addr} at AdressBook')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def add_birthday(self, name, birthday):

        try:

            self.data[name].birthday = Birthday(birthday)
            print(f'For {name} add birthday {birthday} at AdressBook')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')

    def add_contact(self, name):

        if not name in self.data:
            new_record = Record(name)
            self.data[new_record.name.value] = new_record
            print(f'For {name} add contact at AdressBook')

        else:
            print(f'Contact with this name exist. Try other name or other command')

    def add_email(self, name, email):

        try:

            self.data[name].email = Email(email)
            print(f'For {name} add email {email} at AdressBook')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

        except ValueError:
            raise ValueError("Mistake in email, example: my_email@pyton.com")

    def add_phone(self, name, phone):

        try:

            self.data[name].add_phone(phone)
            print(f'For {name} add phone {phone} at AdressBook')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError("Not correct format for phone......")

    def remove_address(self, name):
        try:
            self.data[name].address = ''
            print(f'For {name} delete address at AdressBook')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_birthday(self, name):
        try:
            self.data[name].birthday = ''
            print(f'For {name} delete birthday at AdressBook')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_contact(self, name):

        try:
            self.data.__delitem__(name)
            print(f'Contact {name} has been deleted')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_email(self, name):
        try:
            self.data[name].email = ''
            print(f'For {name} delete email')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_phone(self, name, phone):

        try:
            self.data[name].delete_phone(phone)
            print(f'For {name} delete phone {phone}')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def change_address(self, name, address):

        try:
            self.data[name].address = address
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def change_contact(self, old_name, new_name):

        try:
            record = self.data[old_name]
        except KeyError:
            raise ValueError(f'Contact {old_name} has not been found')

        record.name.value = new_name
        self.data.__delitem__(old_name)
        self.data.__setitem__(new_name, record)
        print(f"Contact's name Name {old_name} has been changed at {new_name}")

    def change_email(self, name, email):

        try:
            self.data[name].email = Email(email)
            print(f'For {name} add email: {email} ')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Mistake in email')

    def change_phone(self, name, old_phone, new_phone):

        try:
            self.data[name].edit_phone(old_phone, new_phone)
            print(f'For {name} phone {old_phone} has changed on {new_phone} ')

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Phone {old_phone} has not been found')

    def change_birthday(self, name, birthday):
        """Change old birthday  for name which is in Contacts to new """

        try:
            self.data[name].birthday = Birthday(birthday)
            print(f'For {name} add birthday {birthday}')
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')

    def find_contact(self, key):
     #       contacts = {}
        print(f'Result of search on key "{key}":')
        count = 0
        key_all = False
# if key in name or key in phone.value or key in str(data.email) or key in data.address:
        for name, data in self.data.items():
            key_is = False
            if key in name:
                key_is = True
            elif key in str(data.email):
                key_is = True
            elif key in data.address:
                key_is = True
            elif key in str(data.birthday):
                key_is = True
            else:
                for phone in data.phones:
                    if key in phone.value:
                        key_is = True
            key_all = key_all or key_is

            if key_is:
                print(f'{self.data[name]}')

        if not key_all:

            print(f'Contacts for {key} not found')

    def save_to_file(self, file_name):
        self.write_adress_book_file()
        print('Data has been saved')

    def show_birthdays(self, days):
        pass

    def show_contact(self, name):

        if name in self.data:
            print(self.data[name])
        else:
            print(
                f'Contact with name {name} not exist. Try other name or other command')

    def show_all_contact(self, number_on_page=None):
        if not number_on_page:
            number_on_page = 3

        stock = self.iterator()
        page = 1

        while True:
            try:
                print(f"Page:   {page}")
                for _ in range(number_on_page):
                    print(next(stock))

                page += 1
            except StopIteration:
                print("it's end.No contacts in book")
                break

    def quit_func(self):
        self.write_adress_book_file()
        return 'Good bye!'
