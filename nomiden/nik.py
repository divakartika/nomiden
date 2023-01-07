from datetime import date, datetime
import pandas as pd
# from data.processing import regioncode as rc

rc = pd.read_csv('data/regioncode.csv')

def province(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2]
        prov = rc.loc[rc['code'] == prov_code, 'region'].item()
        return prov
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def city(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2]
        city_code = f'{prov_code}.{idnum[2:4]}'
        city = rc.loc[rc['code'] == city_code, 'region'].item()
        return city
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def district(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2] # province
        city_code = f'{prov_code}.{idnum[2:4]}' # city
        dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
        dist = rc.loc[rc['code'] == dist_code, 'region'].item()
        return dist
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def gender(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        birth_code = int(idnum[6:8])
        if birth_code >= 1 and birth_code <= 31:
            gend = "Male"
        elif birth_code >= 41 and birth_code <= 71:
            gend = "Female"
        else:
            raise ValueError("Identification number (NIK) invalid, character[6:8] must be between 1 to 71")
        return gend
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def birthdate(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        bdate = bdtm.day
        return bdate
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def birthmonth(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        bmonth = bdtm.month
        return bmonth
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def birthyear(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        byear = bdtm.year
        return byear
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def birthdtm(idnum): # birthday in datetime data type
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        return bdtm
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def birthday(idnum): # birthday in string data type
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        bday = bdtm.strftime("%d %B %Y")
        return bday
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def age(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        bcode = idnum[6:12]
        if int(bcode[:2]) > 31:
            bcode = bcode.replace(bcode[:2], str(int(bcode[:2]) - 40))
        bdtm = datetime.strptime(bcode, "%d%m%y")
        today = date.today()
        age = today.year - bdtm.year - ((today.month, today.day) < (bdtm.month, bdtm.day))
        return age
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def nthperson(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        nth = int(idnum[13:])
        return nth
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 