import re


def check_pwd(mystr):
    pattern1 = re.compile('[a-z]+')
    pattern2 = re.compile('[A-Z]+')
    input_psd = "~`!@#$%^&*()_+-="

    if mystr == '':
        return False

    if len(mystr) < 8 or len(mystr) > 20:
        return False
    match = pattern1.findall(mystr)
    if not match:
        return False
    match2 = pattern2.findall(mystr)
    if not match2:
        return False
    flag = False
    for i in input_psd:
        if i in mystr:
            flag = True
    if not flag:
        return False

    return True
