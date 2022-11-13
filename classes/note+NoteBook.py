from collections import UserDict


class NoteBook(UserDict):
    @staticmethod
    def check_title(func):
        def inner(self, *args):
            flag = self.data.get(args[0], None)
            if flag:
                return func(self, *args)
        return inner

    def add_note(self, title):
        self.data[title] = Note(title)

    def show_note(self, title):
        return self.data.get(title, 'this note doesnt exist')

    def show_all_notes(self, flag=None):
        flag = True if flag == '-r' else False
        count = 0
        constant_number = 5
        data_new = sorted(list(self.data.items()), reverse=flag)
        while count < len(data_new):
            print(data_new[count:count + constant_number])
            user_input = input('nex 5 ?  ')
            if user_input == 'exit':
                break
            else:
                count += constant_number

    def find_note_by_title(self, word):
        return [note for title, note in self.data.items() if word.lower() in title.lower()]

    def find_note_by_tag(self, tag, flag=None):
        flag = True if flag == '-r' else False
        result = [note for note in self.data.values() if tag.lower() in [
            x.lower() for x in note.tags]]
        return sorted(result, key=lambda x: x.title.lower(), reverse=flag)

    @ check_title
    def delete_note(self, title):
        self.data.pop(title)

    @ check_title
    def edit_text(self, title, new_text):
        self.data[title].text = new_text

    @ check_title
    def add_text(self, title, new_words):
        self.data[title].text += '. ' + new_words

    @ check_title
    def add_tag(self, title, new_tag):
        self.data[title].tags.append(new_tag)

    @ check_title
    def remove_tag(self, title, target_tag):
        result = ''.join(list(filter(lambda x: target_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)

    @ check_title
    def change_tag(self, title, old_tag, new_tag):
        result = ''.join(list(filter(lambda x: old_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)
            self.data[title].tags.append(new_tag)


class Note:
    def __init__(self, title):
        self.title = title
        self.text = ''
        self.tags = []

    def __repr__(self):
        return f'{self.title}, {self.text}, {self.tags}'


notebook = NoteBook()


notebook.add_note('Apple')
notebook.add_note('Candy')
notebook.add_note('Bridge')
notebook.add_note('ellisium')
notebook.add_note('doctor')

notebook.add_note('1')
notebook.add_note('2')
notebook.add_note('3')
notebook.add_note('4')
notebook.add_note('5')


notebook.edit_text('Apple', 'Very good fruit')
notebook.edit_text('Candy', 'my favourite')
notebook.edit_text('Bridge', 'Souzh bridge')
notebook.edit_text('ellisium', 'good place')
notebook.edit_text('doctor', 'visit in monday')

notebook.add_tag('Apple', 'fruit')
notebook.add_tag('Candy', 'candy')
notebook.add_tag('Bridge', 'bridge')
notebook.add_tag('ellisium', 'place')
notebook.add_tag('doctor', 'people')
notebook.add_tag('Bridge', 'place')
notebook.add_tag('Apple', 'place')

notebook.change_tag('doctor', 'peopLE', 'HUMANS')
notebook.show_all_notes('-r')
