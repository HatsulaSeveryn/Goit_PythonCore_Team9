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
        flag = True if flag == '-r' else False
        page_number, page_size = int(page_number), int(page_size)
        data_new = list(self.data.items())
        all_note = page_number * page_size
        yield sorted(list(data_new[(all_note - page_size):all_note]), key=lambda x: x[0].lower(), reverse=flag)

    def find_note_by_title(self, word):
        result = []
        for title, note in self.data.items():
            if word.lower() in title.lower():
                result.append(note)
        return result

    def find_note_by_tag(self, tag, flag=None):
        flag = True if flag == '-r' else False
        result = []
        for note in self.data.values():
            new_note_tags = [x.lower() for x in note.tags]
            if tag.lower() in new_note_tags:
                result.append(note)
        return sorted(result, key=lambda x: x.title.lower(), reverse=flag)

    def delete_note(self, title):
        for titl, note in self.data.items():
            if titl.lower() == title.lower():
                self.data.pop(titl)


class Note:
    def __init__(self, title):
        self.title = title
        self.text = ''
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

    def add_text(self, new_text):
        self.text += ' '+new_text

    def __repr__(self):
        return f'{self.title}, {self.text}, {self.tags}'


notebook = NoteBook()


name = Note('One')
name.add_text('hello world')
notebook.add_note(name)
notebook['One'].add_tag('yer')
print(notebook['One'].tags)
