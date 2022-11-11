from classes.field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.isnumeric():
            self.__value = value
        else:
            print('Please for input phone use only number')
            raise TypeError
