def dict_count(given_list):
    # sort_list = sorted(given_list)
    # print(sort_list)
    set_list = set(given_list)
    # print(set_list)

    dictionary = {}
    # count = 0

    for element in set_list:
        dictionary[str(element)] = given_list.count(element)

    # for i in range(len(given_list)):
    #     count = count + 1
    #     if  len(given_list)-1 < i + 1:
    #         dictionary[str(sort_list[i])] = count
    #
    #     elif sort_list[i] != sort_list[i + 1]:
    #         for element in set_list:
    #             dictionary[str(element)] = count
    #         count = 0

    return dictionary
