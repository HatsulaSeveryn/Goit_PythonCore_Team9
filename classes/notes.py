from collections import UserDict


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def show_note(self, title):
        result = 'empty'
        for titl, note in self.data.items():
            if titl.lower() == title.lower():
                result = note
        return result

    def show_all_notes(self, page_number, page_size, flag=None):
        page_number, page_size = int(page_number), int(page_size)
        data_new = list(self.data.items())
        all_note = page_number * page_size
        if not flag:
            yield sorted(list(data_new[(all_note - page_size):all_note]), key=lambda x: x[0].lower())
        elif flag == '-r':
            yield sorted(list(data_new[(all_note - page_size):all_note]), key=lambda x: x[0].lower(), reverse=True)
        else:
            return 'wrong command: try ''-r'' for reverse list'

    def find_note_by_title(self, word):
        result = []
        for title, note in self.data.items():
            if word.lower() in title.lower():
                result.append(note)
        return result

    def find_note_by_tag(self, tag, flag=None):
        result = []
        for note in self.data.values():
            new_note_tags = [x.lower() for x in note.tags]
            if tag.lower() in new_note_tags:
                result.append(note)
        if not flag:
            return sorted(result, key=lambda x: x.title.lower())
        elif flag == '-r':
            return sorted(result, key=lambda x: x.title.lower(), reverse=True)
        else:
            return 'wrong command: try ''-r'' for reverse list'

    def delete_note(self, title):
        for titl, note in self.data.items():
            if titl.lower() == title.lower():
                self.data.pop(titl)


class Note:
    def __init__(self, title, note):
        self.title = title
        self.note = note
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        for tg in self.tags:
            if tag.lower() == tg.lower():
                self.tags.remove(tg)

    def change_tag(self, old_tag, new_tag):
        for tg in self.tags:
            if old_tag.lower() == tg.lower():
                self.tags.remove(tg)
                self.tags.append(new_tag)

    def __repr__(self):
        return f'{self.title}, {self.note}, {self.tags}'


notebook = NoteBook()


first = Note('life planet beautiful', 'Its about our life and other...')
first.add_tag('Life')
first.add_tag('Planet')
second = Note('animal', 'Need to by some puppy')
second.add_tag('plaNET')
fife = Note('Bear', 'gooood')
fife.add_tag('planet')
six = Note('Ceylon tea', 'my favourite')
six.add_tag('PLAnet')
notebook.add_note(first)
notebook.add_note(second)
notebook.add_note(fife)
notebook.add_note(six)
nine = Note('Ellias', 'bad bad')
nine.add_tag('PlaneT')
notebook.add_note(nine)
# print(notebook.data)
# print(notebook.show_note('Animal'))
# notebook.delete_note('bea')
# print(notebook.find_note_by_title('ce'))


def add_tagg():
    adder = notebook.data['animal']
    adder.add_tag('frog')


def remove_tag():
    adder = notebook.data['animal']
    adder.remove_tag('plaN')


def change_tag():
    adder = notebook.data['animal']
    adder.change_tag('planet', 'MINIMALIZM')


add_tagg()
change_tag()

print(notebook.data['animal'])
