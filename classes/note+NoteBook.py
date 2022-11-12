from collections import UserDict


class NoteBook(UserDict):
    def add_note(self, note):
        self.data[note.title] = note

    def show_note(self, title):
        return self.data.get(title, 'this note doesnt exist')

    def show_all_notes(self, page_number, page_size, flag=None):
        flag = True if flag == '-r' else False
        page_number, page_size = int(page_number), int(page_size)
        data_new = list(self.data.items())
        all_note = page_number * page_size
        # yield --> return
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
        result = self.data.get(title, None)
        if result:
            self.data.pop(title)

    def edit_text(self, title, new_text):
        result = self.data.get(title, None)
        if result:
            self.data[title].text = new_text

    def add_piece_to_text(self, title, new_words):
        result = self.data.get(title, None)
        if result:
            self.data[title].text += '. ' + new_words

    def add_tag(self, title, new_tag):
        result = self.data.get(title, None)
        if result:
            self.data[title].tags.append(new_tag)

    def remove_tag(self, title, target_tag):
        result = self.data.get(title, None)
        if result:
            for tag in self.data[title].tags:
                if target_tag.lower() == tag.lower():
                    self.data[title].tags.remove(tag)

    def change_tag(self, title, old_tag, new_tag):
        result = self.data.get(title, None)
        if result:
            for tag in self.data[title].tags:
                if old_tag.lower() == tag.lower():
                    self.data[title].tags.remove(tag)
                    self.data[title].tags.append(new_tag)


class Note:
    def __init__(self, title):
        self.title = title.capitalize()
        self.text = ''
        self.tags = []

    def __repr__(self):
        return f'{self.title}, {self.text}, {self.tags}'


notebook = NoteBook()


one = Note('Black')
two = Note('Apple')
three = Note('Cat')
four = Note('elliot')
five = Note('doctor')

notebook.add_note(one)
notebook.add_note(two)
notebook.add_note(three)
notebook.add_note(four)
notebook.add_note(five)
notebook.edit_text('Black', 'hello world')
notebook.add_piece_to_text('Black', 'and go hell all')
notebook.add_tag('Black', 'Colour')
notebook.add_tag('Black', 'Other')
notebook.change_tag('black', 'other', '777')
print(notebook)
