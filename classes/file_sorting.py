import shutil
import os
from datetime import datetime


class FileSorting:
    map = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
           'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
           'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
           'э': 'e', 'ю': 'yu', 'я': 'ya', 'і': 'i', 'є': 'e', 'ї': 'i',
           'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
           'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
           'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
           'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'І': 'I', 'Є': 'E', 'Ї': 'I'}
    types = {
        'images': ['jpeg', 'png', 'jpg', 'svg', 'webp'],
        'video': ['avi', 'mp4', 'mov', 'mkv'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'pptx'],
        'audio': ['mp3', 'ogg', 'mov', 'amr'],
        'archives': ['zip', 'gz', 'tar']
    }

    def __init__(self, folder_path=''):
        self.check_path(folder_path)
        self.name_folder = folder_path

    @staticmethod
    def check_path(folder_path):
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f'{folder_path} is not exist')
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f'{folder_path} is not a directory')

    def read_folder(self, name_folder=None):
        if not name_folder:
            name_folder = self.name_folder
        return os.listdir(name_folder)

    def check_file_type(self, file):
        file_name_arr = file.split('.')
        file_ext = ''
        if len(file_name_arr) > 1:
            file_ext = file_name_arr[-1]
        if not file_ext:
            return None
        else:
            for key, val in self.types.items():
                if file_ext.lower() in val:
                    return key
            return None

    def rename_file(self, folder_to, folder_from, file):
        path_to = os.path.join(self.name_folder, folder_to)
        if not os.path.exists(path_to):
            os.makedirs(path_to)
        if folder_to != 'archives':
            try:
                os.rename(os.path.join(folder_from, file), os.path.join(path_to, self.normalize(file)))
            except FileExistsError:
                print(f'File {file} is already exist')
                while True:
                    is_rewrite = input(f'Do you want to rewrite file {file} (y/n)').lower()
                    if is_rewrite == 'y':
                        os.replace(os.path.join(folder_from, file), os.path.join(path_to, self.normalize(file)))
                        break
                    elif is_rewrite == 'n':
                        os.rename(os.path.join(folder_from, file), os.path.join(path_to, self.normalize(file, True)))
                        break

        else:
            f = self.normalize(file).split('.')
            try:
                shutil.unpack_archive(os.path.join(folder_from, file), os.path.join(path_to, f[0]), f[1])
            except shutil.ReadError:
                print(f"Archive {os.path.join(folder_from, file)} can't be unpack")
            else:
                os.remove(os.path.join(folder_from, file))

    def normalize(self, file, is_copy=False):
        lists = file.split('.')
        name_file = '.'.join(lists[0:-1])
        new_name = ''
        for el in name_file:
            if el in self.map:
                new_name += self.map[el]
            elif el.isalnum():
                new_name += el
            else:
                new_name += '_'
        if is_copy:
            new_name += f'_(copy_{datetime.now().microsecond})'
        return new_name + '.' + lists[-1]

    def sorting_folder(self, name_folder=None):
        if not name_folder:
            name_folder = self.name_folder
        lists = self.read_folder(name_folder)
        for el in lists:
            path_file = os.path.join(name_folder, el)
            if os.path.isdir(path_file):
                self.sorting_folder(path_file)
            else:
                folder = self.check_file_type(el)
                if folder:
                    self.rename_file(folder, name_folder, el)

    def check_clear_folder(self, name_folder=None):
        if not name_folder:
            name_folder = self.name_folder
        is_remove = False
        lists = os.listdir(name_folder)
        if not lists:
            os.rmdir(name_folder)
            return True
        else:
            for el in lists:
                path_el = os.path.join(name_folder, el)
                if os.path.isdir(path_el):
                    if self.check_clear_folder(path_el):
                        is_remove = True
            if is_remove:
                self.check_clear_folder(name_folder)
                return True

    def sorting(self):
        self.sorting_folder()
        self.check_clear_folder()
        print('All files was sort')