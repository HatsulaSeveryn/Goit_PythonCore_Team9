from collections import UserDict


def check_title(func):
    def inner(self, *args):
        flag = self.data.get(args[0], None)
        if flag:
            return func(self, *args)
        raise IndexError('Wrong title, try something else!')
    return inner


class NoteBook(UserDict):
    def add_note(self, title):
        self.data[title] = Note(title)

    def show_note(self, title):
        print(self.data.get(title, 'this note doesnt exist'))

    def show_all_notes(self, flag=None):
        flag = True if flag == '-r' else False
        count = 0
        constant_number = 5
        data_new = sorted(list(self.data.items()), reverse=flag)
        while count < len(data_new):
            print(data_new[count:count + constant_number])
            if len(data_new[count + constant_number + 1:]) == 0:
                break
            user_input = input('enter -> exit\nelse -> next 5 notes   ')
            if user_input.lower() == 'exit':
                break
            else:
                count += constant_number

    def find_note_by_word(self, word, flag=None):
        flag = True if flag == '-r' else False
        result = [note for title, note in self.data.items()
                  if word.lower() in title.lower() or word.lower() in note.text.lower()]
        print(sorted(result, key=lambda x: x.title.lower(), reverse=flag))

    def find_note_by_tag(self, tag, flag=None):
        flag = True if flag == '-r' else False
        result = [note for note in self.data.values() if tag.lower() in [
            x.lower() for x in note.tags]]
        print(sorted(result, key=lambda x: x.title.lower(), reverse=flag))

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
        else:
            raise ValueError('This tag doesnt exist!')

    @check_title
    def change_tag(self, title, old_tag, new_tag):
        result = ''.join(list(filter(lambda x: old_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)
            self.data[title].tags.append(new_tag)
        else:
            raise ValueError('This tag doesnt exist!')

    @check_title
    def change_note(self, old_title, new_title):
        self.data[new_title] = self.data.pop(old_title)
        self.data[new_title].title = new_title


class Note:
    def __init__(self, title):
        self.title = title
        self.text = ''
        self.tags = []

    def __repr__(self):
        return f'{self.title}, {self.text}, {self.tags}'
