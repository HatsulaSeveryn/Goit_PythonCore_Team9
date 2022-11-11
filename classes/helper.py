import os
import pickle
# from classes.addressBook import AddressBook

class Helper:
    def __init__(self):
        self.handler_command = {
            'hello': self.func_hello, 
            'add contact': self.func_add,
            'remove contact':  self.func_remove,
            'delete contact':  self.func_remove,
            'change contact': self.func_change_name,
            'add address': self.func_add_address,
            'remove address': self.func_remove_address,
            'delete address': self.func_remove_address,
            'change address': self.func_change_addrees,
            'add email': self.func_add_email,
            'remove email': self.func_remove_email,
            'delete email': self.func_remove_email,
            'change email': self.func_change_email,
            'add birthday': self.func_add_birthday,
            'remove birthday': self.func_remove_birthday,
            'delete birthday': self.func_remove_birthday,
            'change birthday': self.func_change_birthday,
            'add phone': self.func_add_phone,
            'remove phone': self.func_remove_phone,
            'delete phone': self.func_remove_phone,
            'change phone': self.func_change_phone,
            'show all contact': self.func_show_all_contact,
            'show contact':  self.func_show_contact,
            'show birthdays': self.func_show_birthdays,
            'find contact': self.func_find_contact,
            'add note': self.func_add_note,
            'remove note': self.func_remove_note,
            'delete note': self.func_remove_note,
            'change note': self.func_change_note,
            'add text': self.func_add_text,
            'remove text': self.func_remove_text,
            'delete text': self.func_remove_text,
            'change text': self.func_change_text,
            'add tag': self.func_add_tag,
            'remove tag': self.func_remove_tag,
            'delete tag': self.func_remove_tag,
            'change tag': self.func_change_tag,
            'show all notes': self.func_show_all_notes,
            'show note': self.func_show_note,
            'find note': self.func_find_note,
            'sort folder': self.func_sort_folder,
            'exit': self.func_exit, 
            'close': self.func_exit, 
            'good buy': self.func_exit,
            'help': self.func_help
            }

        self.max_length_cmd = 3

        # self.addressbook = AddressBook()
        addressbook_path = os.path.join('data', 'addressbook.bin')
        if os.path.exists(addressbook_path) and os.path.isfile(addressbook_path) and os.stat(addressbook_path).st_size > 0:
            with open(addressbook_path, 'rb') as f:
                self.addressbook = pickle.load(f)
        else: 
            self.addressbook = None

        notebook_path = os.path.join('data', 'addressbook.bin')
        if os.path.exists(notebook_path) and os.path.isfile(notebook_path) and os.stat(notebook_path).st_size > 0:
            with open(notebook_path, 'rb') as f:
                self.notebook = pickle.load(f)
        else: 
            self.notebook = None

    def check_args(self, count_args=None, name=None, phone=None, birthday=None, *args):
        if count_args == 1:
            if not name:
                raise ValueError('Enter user name')
        elif count_args == 2:
            if not (name and phone):
                raise ValueError('Give me name and phone please')
        elif count_args == 3:
            if not (name and birthday):
                raise ValueError('Give me name and birthday please')
        return True

    def func_hello(self, *args):
        print('How can I help you?')
        return True

    def func_exit(self):
        with open('data//addressbook.bin', 'wb') as f:
            # pickle.dump(self, f)
            pass
        print('Good bye!')
        return False

    def func_add(self, name=None, phone=None, *args):
        self.check_args(1, name, *args)
        # self.addressbook.add_record(name, phone, *args)
        print(f'Record {name} is add')
        return True

    def func_remove(self, name=None, *args):
        self.check_args(1, name, *args)
        # self.addressbook.remove_record(name)
        print(f'Record {name} is delete')
        return True

    def func_change_name(self, name_old=None, name_new=None, *args):
        self.check_args(2, name_old, name_new, *args)
        # self.addressbook.change_name(name_old, name_new)
        print(f'Name of record {name_old} is change')
        return True

    def func_add_address(self, name, address):
        pass

    def func_remove_address(self, name):
        pass

    def func_change_addrees(self, name, address):
        pass

    def func_add_email(self, name, email):
        pass

    def func_remove_email(self, name):
        pass

    def func_change_email(self, name, email):
        pass

    def func_add_birthday(self,name, birthday, *args):
        self.check_args(2, name, birthday, *args)
        # self.addressbook.add_birthday(name, birthday)
        print(f'Birthday is add into record {name}')
        return True

    def func_remove_birthday(self, name):
        pass

    def func_change_birthday(self, name, birthday, *args):
        self.check_args(3, name, None,  birthday, *args)
        # self.addressbook.change_birthday(name, birthday)
        print(f'Birthday of record {name} is change')
        return True

    def func_add_phone(self, name=None, phone=None, *args):
        self.check_args(1, name, *args)
        # self.addressbook.add_phone(name, phone, *args)
        print(f'Phone is add into record {name}')
        return True

    def func_remove_phone(self, name=None, phone=None, *args):
        self.check_args(2, name, phone, *args)
        # self.addressbook.remove_phone(name, phone, *args)
        print(f'Phone {phone} is delete from record {name}')
        return True

    def func_change_phone(self, name=None, phone_old=None, phone_new=None, *args):
        self.check_args(2, name, phone_old, phone_new, *args)
        # self.addressbook.change_phone(name, phone_old, phone_new)
        print(f'Phone {phone_old} of record {name} is change')
        return True

    def func_show_all_contact(self):
        # self.addressbook.print_addressbook()
        return True

    def func_show_contact(self, name=None, *args):
        self.check_args(1, name, *args)
        # print(self.addressbook.show_phone(name))
        return True

    def func_find_contact(self, key=''):
        result = self.addressbook.find(key)
        # self.addressbook.print_addressbook(result)
        return True

    def func_show_birthdays(self, days):
        pass

    def func_add_note(self, title):
        pass

    def func_remove_note(self, title):
        pass

    def func_change_note(self, title):
        pass

    def func_add_text(self, title, text):
        pass

    def func_remove_text(self, title):
        pass

    def func_change_text(self, title, text):
        pass

    def func_add_tag(self, title):
        pass

    def func_remove_tag(self, title, tag):
        pass

    def func_change_tag(self, title, old_tag, new_tag):
        pass

    def func_show_all_notes(self):
        pass

    def func_show_note(self, title):
        pass

    def func_find_note(self, key):
        pass

    def func_sort_folder(self):
        pass

    def func_help(self):
        print('Commands:')
        print(' - hello')
        print(" - add contact <name> ")
        print(' - remove contact <name>  |  delete contact <name>')
        print(' - change contact <name old> <name new>')

        print(" - add address <name> <address>")
        print(' - remove address <name>  |  delete address <name>')
        print(' - change address <name> <address>')

        print(" - add email <name> <email>")
        print(' - remove email <name>  |  delete email <name>')
        print(' - change email <name> <email>')

        print(' - add birthday <name> <birthday>')    
        print(' - remove birthday <name>  |  delete birthday <name>')    
        print(' - change birthday <name> <birthday>')    

        print(' - add phone <name> <phone>')
        print(' - remove phone <name> <phone>  |  delete phone <name> <phone>')
        print(' - change phone <name> <old phone> <new phone>')

        print(' - show all contacts')
        print(' - show contact <name>')
        print(' - show birthdays <days>')
        print(' - find contact <keys charachters>')

        print(" - add note <title>")
        print(' - remove note <title>  |  delete note <title>')
        print(' - change note <old title> <new title>')

        print(' - add text <title> <text>')    
        print(' - remove text <title>  |  delete text <title>')    
        print(' - change text <title> <text>')    

        print(' - add tag <name> <tag>')
        print(' - remove tag <name> <tag>  |  delete tag <name> <tag>')
        print(' - change tag <name> <old tag> <new tag>')

        print(' - show all notes')
        print(' - show note <title>')
        print(' - find note <keys charachters>')

        print(' - sort folder <folder>')
        print(' - good by || close || exit')
        return True

    def handler(self, cmd):
        command =cmd.split(' ')
        # same commands
        for i in range(self.max_length_cmd, 0, -1):
            if (' '.join(command[0:i]).lower()) in self.handler_command:
                return self.handler_command[' '.join(command[0:i]).lower()](*command[i:])
        # similar command
        list_cmd = set()

        # -- same words
        for i in range(self.max_length_cmd - 1, 0, -1):
            for element in self.handler_command:
                if (' '.join(command[0:i]).lower()) in element:
                    list_cmd.add(element)
            if list_cmd:
                break
        if list_cmd:
            print('Maybe you wanted to use one of this commands:')
            for element in list_cmd:
                print('     ', element)
            return True
        else:
            raise IndexError
    
    def running(self):
        while True:
            cmd = input('Enter command (help - show all commands): ')
            try:
                if not self.handler(cmd):
                    break
            except ValueError as e:
                print(e)
            except IndexError :
                print('Command is wrong')
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)
    