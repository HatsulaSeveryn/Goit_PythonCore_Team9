from collections import UserDict


class NoteBook(UserDict):
    @staticmethod
    def check_title(func):
        def inner(self, *args):
            flag = self.data.get(args[0], None)
            if flag:
                return func(self, *args)
        return inner

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
        return [note for title, note in self.data.items() if word.lower() in title.lower()]

    def find_note_by_tag(self, tag, flag=None):
        flag = True if flag == '-r' else False
        result = [note for note in self.data.values() if tag.lower() in [
            x.lower() for x in note.tags]]
        return sorted(result, key=lambda x: x.title.lower(), reverse=flag)

    @check_title
    def delete_note(self, title):
        self.data.pop(title)

    @check_title
    def edit_text(self, title, new_text):
        self.data[title].text = new_text

    @check_title
    def add_text(self, title, new_words):
        self.data[title].text += '. ' + new_words

    @check_title
    def add_tag(self, title, new_tag):
        self.data[title].tags.append(new_tag)

    @check_title
    def remove_tag(self, title, target_tag):
        result = ''.join(list(filter(lambda x: target_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)

    @check_title
    def change_tag(self, title, old_tag, new_tag):
        result = ''.join(list(filter(lambda x: old_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)
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
notebook.add_tag('Cat', 'colour')
notebook.edit_text('Black', 'hello world')
notebook.add_text('Black', 'and go hell all')
notebook.add_tag('Black', 'Colour')
notebook.add_tag('Black', 'Other')
notebook.add_tag('elliot', 'Colour')
notebook.add_tag('Apple', 'colour')
print(notebook.change_tag('Black', 'Colour', '!!!!!!!!!!!!!!!!'))

print(notebook)
print(notebook)
