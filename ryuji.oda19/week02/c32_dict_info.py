def dict_info(FName,LName,EMail,TEL):
    dict = {'firstname': FName,
            'lastname':LName,
            'email': EMail,
            'phone':TEL}
    dict[0].title()
    dict[1].UpperCase()
    return dict

print(dict_info('Ryu','Oda','u.com','025'))

