from datetime import date, datetime
from data import regioncode as rc

def province(idnum):
    idnum = str(idnum)
    prov_code = idnum[:2]
    prov = rc.loc[rc['code'] == prov_code, 'region'].item()
    return prov

def city(idnum):
    idnum = str(idnum)
    prov_code = idnum[:2]
    city_code = f'{prov_code}.{idnum[2:4]}'
    city = rc.loc[rc['code'] == city_code, 'region'].item()
    return city

def district(idnum):
    idnum = str(idnum)
    prov_code = idnum[:2] # province
    city_code = f'{prov_code}.{idnum[2:4]}' # city
    dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
    dist = rc.loc[rc['code'] == dist_code, 'region'].item()
    return dist

def gender(idnum):
    idnum = str(idnum)
    birth_code = int(idnum[6:8])
    if birth_code >= 1 and birth_code <= 31:
        gend = "Male"
    elif birth_code >= 41 and birth_code <= 71:
        gend = "Female"
    else:
        raise("idnum[6:8] must be between 1 to 71")
    return gend

def birthdate(idnum):
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bdate = bdtm.day
    return bdate

def birthmonth(idnum):
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bmonth = bdtm.month
    return bmonth

def birthyear(idnum):
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    byear = bdtm.year
    return byear

def birthdtm(idnum): # birthday in datetime data type
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    return bdtm

def birthday(idnum): # birthday in string data type
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    bday = bdtm.strftime("%d %B %Y")
    return bday

def age(idnum):
    idnum = str(idnum)
    bcode = idnum[6:12]
    if int(bcode[:2]) > 31:
        bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
    bdtm = datetime.strptime(bcode, "%d%m%y")
    today = date.today()

    age = today.year - bdtm.year - ((today.month, today.day) < (bdtm.month, bdtm.day))
    return age

def nthperson(idnum):
    nth = int(idnum[13:])
    return nth