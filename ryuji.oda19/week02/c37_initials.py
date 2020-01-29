def initials(given_list):
    rtn = []

    for i in range(len(given_list)):
        rtn.append(given_list[i][0].upper())

    return rtn

#
# print(initials(['World','Wide','Web']))
# print(initials(['Good','luck','have','fun']))
# print(initials([]))
