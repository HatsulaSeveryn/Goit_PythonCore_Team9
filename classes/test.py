from collections import UserList


class NoteBook(UserList):
    def add_note(self, notes):
        self.data.append(notes)

    def find_notes_by_text(self, symbols):
        result = []
        for note in self.data:
            if symbols in note.note:
                result.append(note)
        return result

    def find_notes_by_tag(self, tag):
        result = []
        for word in self.data:
            if tag in word.tags:
                result.append(word)
        return result


class Notes:
    def __init__(self, note):
        self.note = note
        self.tags = []

    def add_tags(self, tag):
        self.tags.append(tag)

    def __repr__(self):
        return f'{self.note}, {self.tags}'


notebook = NoteBook()
first = Notes('Hello, my name is Igor, and i study')
second = Notes('My good Hello question to you')
second.add_tags('study')
second.add_tags('person')
first.add_tags('person')

notebook.add_note(first)
notebook.add_note(second)
print(notebook.find_notes_by_tag('study'))
