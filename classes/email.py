from classes.field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        try:

            self.__value = value
        # If the date validation goes wrong
        except:
            print("Incorrect data format for email, should be ***@.***.**")
            raise TypeError
