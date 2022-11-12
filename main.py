from classes import AddressBook

contacts_book = AddressBook()

contacts_book.show_all_contact()
print('It is my contants for now')
contacts_book.add_contact('Tom')
contacts_book.add_contact('Jec')
contacts_book.add_phone('Tom', '111')
contacts_book.add_contact('Tom')
contacts_book.add_contact('ggg')
contacts_book.add_email('rewt', 'fss@ddfs.ff')
contacts_book.add_phone('Tom', '334')


contacts_book.add_birthday('Tom', '24.03.1998')
contacts_book.add_birthday('yyy', '17.03.1998')
contacts_book.add_phone('gdg', '111')
contacts_book.change_phone('Tom', '334', '333')
contacts_book.add_address('Tom', 'fdsghdht')
contacts_book.show_all_contact()

contacts_book.add_address('rewt', 'sdg')

contacts_book.change_phone('Tom', '334', '777')
contacts_book.change_address('Tom', 'erwew')
contacts_book.change_email('yyy', 'yyy@fdsg.h')
contacts_book.change_email('rewt', 'eer@fdsg.h')
contacts_book.change_birthday('Tom', '11.11.2233')
contacts_book.remove_contact('ggg')
#contacts_book.remove_phone('Tom', '333')
contacts_book.remove_phone('Tom', '222')
contacts_book.remove_address('Tom')
contacts_book.remove_email('rewt')
contacts_book.remove_birthday('yyy')
#contacts_book.add_phone('gdg', 'fdg')
#contacts_book.change_birthday('Tom', '444')
#contacts_book.add_birthday('we', '2403..98')
#contacts_book.remove_phone('ewqttqq', '222')
# print(contacts_book.values)

contacts_book.show_all_contact()
contacts_book.quit_func()
