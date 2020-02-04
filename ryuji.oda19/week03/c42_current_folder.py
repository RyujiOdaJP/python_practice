import os


def current_folder():
    # dirpath = os.getcwd()
    files = os.listdir()
    dictionary = {}
    dictionary.setdefault('filename')
    dictionary.setdefault('type')
    List = []
    # print(dirpath)
    # print(files)

    for i in range(len(files)):
        types_file = os.path.isfile(files[i])
        types_dir = os.path.isdir(files[i])

        if types_file:
            dictionary['filename'] = files[i]
            dictionary['type'] = 'File'
            List.append(dictionary)
            dictionary = {}

        elif types_dir:
            dictionary['filename'] = files[i]
            dictionary['type'] = 'Folder'
            List.append(dictionary)
            dictionary = {}

    return List


print(current_folder())
