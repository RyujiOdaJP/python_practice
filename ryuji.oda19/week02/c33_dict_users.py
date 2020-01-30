def dict_users (give):

    if give == []:
        return []

    s = []
    dict = {}
    # dict.setdefault('username')
    # dict.setdefault('ID')
    # print(dict)
    for i in range(len(give)):
        dict = {}
        dict.setdefault('username')
        dict.setdefault('ID')
        # dict = {}
        # dict.setdefault('username',[]).append(give[i])
        # dict.setdefault("ID",[]).append(i+1)
        dict['username'] = give[i]
        dict['ID'] = i + 1

        s.append(dict)
        # print(s)
    return s

print(dict_users(['A', 'B', 'C', 'D', 'E']))
# print(dict_users([]))
