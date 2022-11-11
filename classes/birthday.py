from datetime import datetime
from classes.field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        date_format = '%d.%m.%Y'
        # using try-except blocks for handling the exceptions
        try:
            date_birthday = datetime.strptime(value, date_format)
            self.__value = date_birthday
        # If the date validation goes wrong
        except:
            print("Incorrect data format for birthday, should be DD.MM.YYYY")
            raise TypeError

    def __str__(self):
        return datetime.strftime(self.__value, '%d.%m.%Y')
