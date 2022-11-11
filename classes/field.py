class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str_(self):
        return self.value

    def is_contain(self, key):
        if key in self.value:
            return True
        return False
