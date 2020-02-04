import os


class Eraser:

    @staticmethod
    def remove_file(filename):

        try:
            os.remove(filename)
            return '1'

        except FileNotFoundError:
            return '0'

    @staticmethod
    def remove_folder(folder_name):

        try:
            os.rmdir(folder_name)
            return '1'

        except FileNotFoundError:
            return '0'


# print(Eraser().remove_folder('test'))
