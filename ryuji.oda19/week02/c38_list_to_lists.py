def list_to_lists(given):
    rtn = []
    li = []

    # this loop depends on list range
    for i in range(len(given)):
        li.append(rtn)
        # print(rtn)

        # this loop depends on word range

        for x in range(len(given[i])):
            rtn.append(given[i][-x-1])
        rtn = []


        #for x in range(len(given[i])):
            #li[i].append(rtn.append(given[i][-x-1]))

    return li



print(list_to_lists(['Hello']))
print(list_to_lists(['A','a','B','b']))
print(list_to_lists(['Hello','World']))
