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
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise ValueError(f'Identification number (KK) {len(idnum)} characters, length should be 16')

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

def regdate(idnum):
    idnum = _check_length(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rdate = rdtm.day
    return rdate

def regmonth(idnum):
    idnum = _check_length(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rmonth = rdtm.month
    return rmonth

def regyear(idnum):
    idnum = _check_length(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    ryear = rdtm.year
    return ryear

def regdtm(idnum): # registration day in datetime data type
    idnum = _check_length(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    return rdtm

def regday(idnum): # registration day in string data type
    idnum = _check_length(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rday = rdtm.strftime("%d %B %Y")
    return rday

def nthpub(idnum):
    idnum = _check_length(idnum)
    nth = int(idnum[13:])
    return nth

def kkreader(idnum):
    kk_dict = {'NIK': idnum, 'province': province(idnum), 'city': city(idnum), 'district': district(idnum),
            'regist_datetime': regdtm(idnum), 'regist_day': regday(idnum),
            'regist_code': nthpub(idnum)}

    return kk_dict