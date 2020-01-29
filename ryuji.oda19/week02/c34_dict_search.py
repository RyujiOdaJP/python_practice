info_students = {'username': 'sabbe_k', 'score': 100, 'comment': 'Good job!'}


def dict_search(import_dict, key):
    try:
        return import_dict[key]
    except KeyError:
        return "ERROR: '" + key + "' key not found."

# print(dict_search(info_students, 'comment'))
