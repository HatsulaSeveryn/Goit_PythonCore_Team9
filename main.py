from classes import AddressBook

contacts_book = AddressBook()

contacts_book.add_contact('Tom')
contacts_book.add_contact('Jec')
contacts_book.add_phone('Tom', '111')
contacts_book.add_contact('Tom')
contacts_book.add_contact('ggg')

contacts_book.add_phone('Tom', '334')
contacts_book.remove_contact('ggg')
contacts_book.show_all_contact()
contacts_book.add_birthday('Tom', '24.03.1998')
contacts_book.add_birthday('yyy', '17.03.1998')
contacts_book.add_phone('gdg', '111')
contacts_book.change_phone('Tom', '334', '333')
contacts_book.add_address('Tom', 'fdsghdht')
contacts_book.add_address('rewt', 'sdg')
contacts_book.add_address('rewt', 'ssf@ddfs.ff')
contacts_book.change_phone('Tom', '334', '777')
contacts_book.remove_phone('Tom', '333')
contacts_book.remove_phone('Tom', '222')
#contacts_book.remove_phone('ewqttqq', '222')
# print(contacts_book.values)

contacts_book.show_all_contact()
