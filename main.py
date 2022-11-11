from classes import AddressBook

contacts_book = AddressBook()

contacts_book.add_contact('Tom')
contacts_book.add_contact('Jec')
contacts_book.add_phone('Tom', '111')
contacts_book.add_contact('Tom')
contacts_book.add_contact('ggg')
contacts_book.show_all_contact()
contacts_book.add_phone('Tom', '334')
contacts_book.remove_contact('ggg')


# print(contacts_book.values)

contacts_book.show_all_contact()
