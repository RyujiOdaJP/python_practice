def dict_info(FName, LName, EMail, TEL):
    dict = {'firstname':'','lastname': '',
            'email':'', 'phone': ''}

    dict['firstname'] = FName.title()
    dict['lastname'] = LName.upper()
    dict['email'] = EMail
    dict['phone'] = TEL

    return dict
