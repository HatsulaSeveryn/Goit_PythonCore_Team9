import re
from classes.field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        pattern = "[^@]+@[^@]+\.[^@]+"

        if not re.match(pattern, value):
            raise ValueError('This email is not correct')

        self.__value = value
