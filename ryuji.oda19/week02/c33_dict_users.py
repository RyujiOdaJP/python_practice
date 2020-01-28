def dict_users (give):

    s = []
    for i in range(len(give)):
        dict = {}
        dict.setdefault('username',[]).append(give[i])
        dict.setdefault("ID",[]).append(i+1)
        s.append(dict)
    return s

