from collections import UserDict


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def find_note(self, word):
        result = []
        for title, note in self.data.items():
            if word in title:
                result.append(note)
        return result


class Note:
    def __init__(self, title, note):
        self.title = title
        self.note = note
        self.tags = []

    def add_tags(self, tag):
        self.tags.append(tag)

    def __repr__(self):
        return f'{self.title}, {self.note}, {self.tags}'


notebook = NoteBook()

first = Note('Life planet beautiful', 'Its about our life and other...')
second = Note('Animal planet', 'Need to by some puppy')
notebook.add_note(first)
notebook.add_note(second)
print(notebook.find_note('planet'))
