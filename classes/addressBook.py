from collections import UserDict
from classes.birthday import Birthday
from classes.email import Email
from classes.record import Record


class AddressBook(UserDict):

    def iterator(self):
        for record in self.data.values():
            yield record

    def add_address(self, name, addr):
        try:
            if self.data[name].address:
                raise ValueError(
                    f'Contact already have address. Did you want to change it? Use change address command instead')

            self.data[name].address = addr

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def add_birthday(self, name, birthday):

        try:
            if self.data[name].birthday:
                raise ValueError(
                    f'Contact already have birthday. Did you want to change it? Use change birthday command instead')

            self.data[name].birthday = Birthday(birthday)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.1970')

    def add_contact(self, name):

        if name not in self.data:
            new_record = Record(name)
            self.data[new_record.name.value] = new_record

        else:
            raise ValueError(
                f'Contact with this name exist. Try other name or other command')

    def add_email(self, name, email):

        try:
            if self.data[name].email:
                raise ValueError(
                    f'Contact already have email. Did you want to change it? Use change email command instead')

            self.data[name].email = Email(email)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

        except ValueError:
            raise ValueError("Mistake in email, example: my_email@pyton.com")

    def add_phone(self, name, phone):

        try:
            for ph in self.data[name].phones:
                if ph.value == phone:
                    raise ValueError(
                        f'Contact already have that phone. Did you want to change it? Use change phone command instead')

            self.data[name].add_new_phone(phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError("Use only number for phone. Example: 32457")

    def change_address(self, name, address):

        try:
            self.data[name].address = address
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def change_birthday(self, name, birthday):
        """Change old birthday  for name which is in Contacts to new """

        try:
            self.data[name].birthday = Birthday(birthday)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')

    def change_contact(self, old_name, new_name):

        try:
            record = self.data[old_name]
        except KeyError:
            raise ValueError(f'Contact {old_name} has not been found')

        record.name.value = new_name
        self.data.__delitem__(old_name)
        self.data.__setitem__(new_name, record)

    def change_email(self, name, email):

        try:
            self.data[name].email = Email(email)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Mistake in email')

    def change_phone(self, name, old_phone, new_phone):

        try:
            self.data[name].edit_phone(old_phone, new_phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Phone {old_phone} has not been found')

    def find_contact(self, key):
        # if key in name or key in phone.value or key in str(data.email) or key in data.address:
        print(f'Result of search on key "{key}" :')

        key_all = False

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

    def remove_address(self, name):
        try:
            self.data[name].address = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_birthday(self, name):
        try:
            self.data[name].birthday = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_contact(self, name):

        try:
            self.data.__delitem__(name)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_email(self, name):
        try:
            self.data[name].email = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_phone(self, name, phone):

        try:
            self.data[name].delete_phone(phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

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

    def show_birthdays(self, days):

        list_birthday = []

        for rec in self.data.values():

            if rec.birthday:
                days_to = rec.days_to_birthday()

                if days_to <= days:
                    list_birthday.append(rec)
                    print(
                        f"{rec.name}'s birthday is in {str(days_to)} days")

    def show_contact(self, name):

        if name in self.data:
            print(self.data[name])
        else:
            print(
                f"Contact with the name '{name}' does not exist. Try a different name.")


'''
    def __init__(self, filename='address_book.txt'):
        super().__init__()
        self.filename = filename
        self.read_address_book_from_file()

   def quit_func(self):
        self.write_address_book_file()
        return 'Good bye!'
    def write_address_book_file(self):
        with open('address_book.txt', 'wb') as file:
            pickle.dump(self.data, file)

    def read_address_book_from_file(self):
        try:
            with open('address_book.txt', 'rb') as file:
                self.data = pickle.load(file)
                return self.data
        except FileNotFoundError:
            pass
    def save_to_file(self, file_name):
        self.write_address_book_file()
        print('Data has been saved')

         '''
