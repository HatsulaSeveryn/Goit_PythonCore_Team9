import os
import pickle

from classes.file_sorting import FileSorting
from data import constants

# from classes.addressBook import AddressBook

class Helper:
    def __init__(self):
        self.handler_command = {
            'hello': self.func_hello, 
            'add contact': self.func_add_contact,
            'remove contact':  self.func_remove_contact,
            'delete contact':  self.func_remove_contact,
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
            'find tag': self.func_find_tag,
            'sort folder': self.func_sort_folder,
            'exit': self.func_exit, 
            'close': self.func_exit, 
            'good buy': self.func_exit,
            'help': self.func_help
            }
        self.max_length_cmd = 3
        self.sorter = None
        # self.addressbook = AddressBook()
        self.addressbook_path = os.path.join('data', 'addressbook.bin')
        if os.path.exists(self.addressbook_path) and os.path.isfile(self.addressbook_path) and os.stat(self.addressbook_path).st_size > 0:
            with open(self.addressbook_path, 'rb') as f:
                self.addressbook = pickle.load(f)
        else: 
            self.addressbook = None

        self.notebook_path = os.path.join('data', 'notebook.bin')
        if os.path.exists(self.notebook_path) and os.path.isfile(self.notebook_path) and os.stat(self.notebook_path).st_size > 0:
            with open(self.notebook_path, 'rb') as f:
                self.notebook = pickle.load(f)
        else: 
            self.notebook = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.addressbook_path, 'wb') as f:
            pickle.dump(self.addressbook, f)
        with open(self.notebook_path, 'wb') as f:
            pickle.dump(self.notebook, f)

    def check_args(self, count_args=None, more=None, text_err='Invalid number of arguments.', *args):
        args = [value for value in args if value != None and value !='']
        if (more == 0 and (len(args) != count_args)) or (more == 1 and (len(args) <= count_args)):
            raise ValueError(text_err)

    def func_hello(self, *args):
        print('How can I help you?')

    def func_exit(self):
        print('Good bye!')
        quit()

    def func_add_contact(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        # self.addressbook.add_contact(name)
        print(f'Contact {name} is added')

    def func_remove_contact(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        # self.addressbook.remove_contact(name)
        print(f'Contact {name} deleteed')

    def func_change_name(self, name_old=None, name_new=None, *args):
        err = "Give me old contact's name and new contact's name. Contact's name can consist of 1 word only"
        self.check_args(2, 0, err, name_old, name_new, *args)
        # self.addressbook.change_contact(name_old, name_new)
        print(f'Name of record {name_old} changed')

    def func_add_address(self, name=None, *args):
        err = "Give me contact's name and address"
        self.check_args(2, 1, err, name, *args)
        address = ' '.join(args)
        # self.addressbook.add_address(name, address)
        print(f'Address {address} added for contact {name}')

    def func_remove_address(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        address = ' '.join(args)
        # self.addressbook.remove_address(name)
        print(f'Address {address} remove for record {name}')

    def func_change_addrees(self, name=None, *args):
        err = "Give me contact's name and address."
        self.check_args(2, 1, err, name, *args)
        address = ' '.join(args)
        # self.addressbook.change_address(name, address)
        print(f'Address changed for contact {name}')

    def func_add_email(self, name=None, email=None, *args):
        err = "Give me contact's name and email"
        self.check_args(2, 0, err, name, email, *args)
        # self.addressbook.add_email(name, email)
        print(f'E-mail {email} added for contact {name}')

    def func_remove_email(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        # self.addressbook.remove_email(name)
        print(f'E-mail removed for contact {name}')

    def func_change_email(self, name=None, email=None, *args):
        err = "Give me contact's name and email."
        self.check_args(2, 0, err, name, email, *args)
        # self.addressbook.change_email(name, email)
        print(f'E-mail changed for contact {name}')

    def func_add_birthday(self, name=None, birthday=None, *args):
        err = "Give me contact's name and date of birth."
        self.check_args(2, 0, err, name, birthday, *args)
        # self.addressbook.add_birthday(name, birthday)
        print(f'Date of birth {birthday} added for contact {name}')

    def func_remove_birthday(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        # self.addressbook.remove_birthday(name)
        print(f'Date of birth removed for contact {name}')

    def func_change_birthday(self, name=None, birthday=None, *args):
        err = "Give me contact's name and date of birth."
        self.check_args(2, 0, err, name, birthday, *args)
        # self.addressbook.change_birthday(name, birthday)
        print(f'Date of birth changed for contact {name}')

    def func_add_phone(self, name=None, phone=None, *args):
        err = "Give me contact's name and phone."
        self.check_args(2, 0, err, name, phone, *args)
        # self.addressbook.add_phone(name, phone)
        print(f'Phone {phone} added for contact {name}')

    def func_remove_phone(self, name=None, phone=None, *args):
        err = "Give me contact's name and phone."
        self.check_args(2, 0, err, name, phone, *args)
        # self.addressbook.remove_phone(name, phone)
        print(f'Phone {phone} removed for contact {name}')

    def func_change_phone(self, name=None, phone_old=None, phone_new=None, *args):
        err = "Give me contact's name, old phone and new phone."
        self.check_args(3, 0, err, name, phone_old, phone_new, *args)
        # self.addressbook.change_phone(name, phone_old, phone_new)
        print(f'Phone {phone_old} changed for contact {name}')

    def func_show_all_contact(self):
        pass
        # self.addressbook.print_addressbook()

    def func_show_contact(self, name=None, *args):
        err = "Give me contact's name. Contact's name can consist of 1 word only"
        self.check_args(1, 0, err, name, *args)
        # self.addressbook.show_contact(name)

    def func_find_contact(self, key='', *args):
        if args:
            raise ValueError('Give me one key word.')
        # self.addressbook.find_contact(key)

    def func_show_birthdays(self, days, *args):
        if args:
            raise ValueError('Give me amount days to birthdays only.')
        # self.addressbook.show_birthdays(days)

    def func_add_note(self, title=None, *args):
        err = "Give me title for note. Title can consist of 1 word only"
        self.check_args(1, 0, err, title, *args)
        # self.notebook.add_note(title)
        print(f'Note with title "{title}" added')

    def func_remove_note(self, title=None, *args):
        err = "Give me title for note. Title can consist of 1 word only"
        self.check_args(1, 0, err, title, *args)
        # self.notebook.delete_note(title)
        print(f'Note with title "{title}" removed')

    def func_change_note(self, title_old=None, title_new=None, *args):
        err = "Give me old title and new title for note. Title can consist of 1 word only"
        self.check_args(2, 0, err, title_old, title_new, *args)
        # self.notebook.change_note(title, *args)
        print(f'Title "{title_old}" changed')

    def func_add_text(self, title=None, *args):
        err = "Give me title and text for note."
        self.check_args(2, 1, err, title, *args)
        text = ' '.join(args)
        # self.notebook.add_text(title, text)
        print(f'Text for note with "{title}" added')

    def func_remove_text(self, title=None, *args):
        err = "Give me title for note."
        self.check_args(1, 0, err, title, *args)
        # self.notebook.edit_text(title, '')
        print(f'Text for note with "{title}" removed')

    def func_change_text(self, title=None, *args):
        err = "Give me title and text for note."
        self.check_args(2, 1, err, title, *args)
        text = ' '.join(args)
        # self.notebook.edit_text(title, text)
        print(f'Text for note with "{title}" added')

    def func_add_tag(self, title=None, tag=None, *args):
        err = "Give me title and tag for note."
        self.check_args(2, 0, title, tag, *args)
        # self.notebook.add_tag(title, tag)
        print(f'Tag {tag} added for note with title "{title}"')

    def func_remove_tag(self, title=None, tag=None, *args):
        err = "Give me title and tag for note."
        self.check_args(2, 0, title, tag, *args)
        # self.notebook.remove_tag(name, tag)
        print(f'Tag {tag} removed for note with title "{title}"')

    def func_change_tag(self, title=None, old_tag=None, new_tag=None, *args):
        err = "Give me title, old tag and new tag for note."
        self.check_args(3, 0, title, old_tag, new_tag, *args)
        # self.notebook.change_tag(name, old_tag, new_tag)
        print(f'Tag {old_tag} changed for note with title "{title}"')

    def func_show_all_notes(self):
        pass
        # self.notebook.show_all_notes()

    def func_show_note(self, title=None, *args):
        err = "Give me title for note."
        self.check_args(1, 0, title, *args)
        # print(self.notebook.show_note(title))

    def func_find_note(self, key=None, flag=None, *args):
        if (flag != '-r' and flag != None) or args:
            raise ValueError('Give me one key word and if its need flag(-r for reverse sort).')
        # result = self.notebook.find_note_by_title(key, flag)
        # print(result)

    def func_find_tag(self, tag=None, flag=None, *args):
        if (flag != '-r' and flag != None) or args:
            raise ValueError('Give me one tag and if its need flag(-r for reverse sort).')
        # result = self.notebook.find_note_by_tag(tag, flag)
        # self.notebook.print_addressbook(result)

    def func_sort_folder(self, folder, *args):
        err = 'Give me one folder for sorting'
        self.check_args(1, 0, err, folder, *args)
        sorter = FileSorting(folder)
        sorter.sorting()

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
        print(' - find note <keys charachters> {-r (for reverse sort)}')
        print(' - find tag <tag> {-r (for reverse sort)}')

        print(' - sort folder <folder>')
        print(' - good by || close || exit')

    def handler(self, cmd):
        command =cmd.strip().split(' ')
        # same commands
        for i in range(self.max_length_cmd, 0, -1):
            if (' '.join(command[0:i]).lower()) in self.handler_command:
                return self.handler_command[' '.join(command[0:i]).lower()](*command[i:])
        # similar command
        list_cmd = set()
        # -- Levenstain
        for el in self.handler_command:
            count = len(el.split(' '))
            for i in range(count, 0, -1):
                c = ' '.join(command[0:i]).lower()
                result = self.levenstein(el, c) * 100 / len(el)
                if result < 40:
                    list_cmd.add(el)
        # -- rearranged words
        for element_handler in self.handler_command:
            cmd_range = element_handler.split(' ')
            founded = True
            for element_cmd in command:
                if element_cmd not in cmd_range:
                    founded = False
            if founded:
                list_cmd.add(element_handler)
        # -- same words
        for i in range(self.max_length_cmd - 1, 0, -1):
            for element in self.handler_command:
                check_cmd = ' '.join(command[0:i]).lower()
                cnt = len(element.split(' ')[0])
                if element.startswith(check_cmd[0:cnt]) or element.split(' ')[0] in check_cmd:
                # if element.startswith(' '.join(command[0:i]).lower()):
                    list_cmd.add(element)
            if list_cmd:
                    break
        # -- similar word
        if not list_cmd:
            pass
        if list_cmd:
            print('Maybe you wanted to use one of this commands:')
            for element in list_cmd:
                print('     ', element)
        else:
            raise IndexError('Command is wrong')
    
    def running(self):
        while True:
            cmd = input('Enter command (help - show all commands): ')
            try:
                self.handler(cmd)
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)
    
    def levenstein(self, str_1, str_2):
        n, m = len(str_1), len(str_2)
        if n > m:
            str_1, str_2 = str_2, str_1
            n, m = m, n
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if str_1[j - 1] != str_2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]
