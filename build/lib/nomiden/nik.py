import os
from datetime import date, datetime
import pandas as pd

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "regioncode.csv")
rc = pd.read_csv(DATA_PATH)

def _check_length(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        return idnum
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise ValueError(f'Identification number (NIK) {len(idnum)} characters, length should be 16')

def province(idnum):
    idnum = _check_length(idnum)
    prov_code = idnum[:2]
    prov = rc.loc[rc['code'] == prov_code, 'region'].item()
    return prov

def city(idnum):
    idnum = _check_length(idnum)
    prov_code = idnum[:2]
    city_code = f'{prov_code}.{idnum[2:4]}'
    city = rc.loc[rc['code'] == city_code, 'region'].item()
    return city

def district(idnum):
    idnum = _check_length(idnum)
    prov_code = idnum[:2] # province
    city_code = f'{prov_code}.{idnum[2:4]}' # city
    dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
    dist = rc.loc[rc['code'] == dist_code, 'region'].item()
    return dist

def gender(idnum):
    idnum = _check_length(idnum)
    gend_code = int(idnum[6:8])
    if gend_code >= 1 and gend_code <= 31:
        gend = "Male"
    elif gend_code >= 41 and gend_code <= 71:
        gend = "Female"
    else:
        raise ValueError("Identification number (NIK) invalid, character[6:8] must be between 1 to 71")
    return gend

def birthdate(idnum):
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bdate = bdtm.day
    return bdate

def birthmonth(idnum):
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bmonth = bdtm.month
    return bmonth

def birthyear(idnum):
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    byear = bdtm.year
    return byear

def birthdtm(idnum): # birthday in datetime data type
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    return bdtm

def birthday(idnum): # birthday in string data type
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bday = bdtm.strftime("%d %B %Y")
    return bday

def age(idnum):
    idnum = _check_length(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    today = date.today()
    age = today.year - bdtm.year - ((today.month, today.day) < (bdtm.month, bdtm.day))
    return age

def nthperson(idnum):
    idnum = _check_length(idnum)
    nth = int(idnum[13:])
    return nth

def nikreader(idnum):
    idnum = _check_length(idnum)
    nik_dict = {'NIK': idnum, 'province': province(idnum), 'city': city(idnum), 'district': district(idnum),
            'gender': gender(idnum), 'birth_datetime': birthdtm(idnum), 'birthday': birthday(idnum),
            'age': age(idnum), 'regist_code': nthperson(idnum)}

    return nik_dict