from collections import UserDict


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def find_note_by_word(self, word):
        result = []
        for title, note in self.data.items():
            if word.lower() in title.lower():
                result.append(note)
        return result

    def find_note_by_tag(self, tag):
        result = []
        for note in self.data.values():
            new_note_tags = [x.lower() for x in note.tags]
            if tag.lower() in new_note_tags:
                result.append(note)
        return sorted(result, key=lambda x: x.title.lower())


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

first = Note('life planet beautiful', 'Its about our life and other...')
first.add_tags('Life')
first.add_tags('Planet')
second = Note('Animal', 'Need to by some puppy')
second.add_tags('plaNET')
fife = Note('Bear good', 'gooood')
fife.add_tags('planet')
six = Note('Ceylon tea', 'my favourite')
six.add_tags('PLAnet')
notebook.add_note(first)
notebook.add_note(second)
notebook.add_note(fife)
notebook.add_note(six)
nine = Note('Ellias', 'bad bad')
nine.add_tags('PlaneT')
notebook.add_note(nine)
print(notebook.find_note_by_word('beautiful'))
