import os
from typing import Union
from datetime import date, datetime
import pandas as pd

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "regioncode.csv")
rc = pd.read_csv(DATA_PATH)

def _check_length(idnum: Union[str, int]) -> str:
    idnum = str(idnum)
    if len(idnum) == 16:
        return idnum
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise ValueError(f'Identification number (KK) {len(idnum)} characters, length should be 16')

def _check_reg(idnum: str) -> datetime:
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40), 1)
    rdtm = datetime.strptime(rcode, "%d%m%y")
    now = datetime.now()
    if rdtm > now:
        rdtm = rdtm.replace(year = rdtm.year - 100)
    return rdtm

def province(idnum: Union[str, int]) -> str:
    idnum = _check_length(idnum)
    prov_code = idnum[:2]
    prov = rc.loc[rc['code'] == prov_code, 'region'].item()
    return prov

def city(idnum: Union[str, int]) -> str:
    idnum = _check_length(idnum)
    prov_code = idnum[:2]
    city_code = f'{prov_code}.{idnum[2:4]}'
    city = rc.loc[rc['code'] == city_code, 'region'].item()
    return city

def district(idnum: Union[str, int]) -> str:
    idnum = _check_length(idnum)
    prov_code = idnum[:2] # province
    city_code = f'{prov_code}.{idnum[2:4]}' # city
    dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
    dist = rc.loc[rc['code'] == dist_code, 'region'].item()
    return dist

def regdate(idnum: Union[str, int]) -> int:
    idnum = _check_length(idnum)
    rdtm = _check_reg(idnum)
    rdate = rdtm.day
    return rdate

def regmonth(idnum: Union[str, int]) -> int:
    idnum = _check_length(idnum)
    rdtm = _check_reg(idnum)
    rmonth = rdtm.month
    return rmonth

def regyear(idnum: Union[str, int]) -> int:
    idnum = _check_length(idnum)
    rdtm = _check_reg(idnum)
    ryear = rdtm.year
    return ryear

def regdtm(idnum: Union[str, int]) -> datetime: # registration day in datetime data type
    idnum = _check_length(idnum)
    rdtm = _check_reg(idnum)
    return rdtm

def regday(idnum: Union[str, int]) -> str: # registration day in string data type
    idnum = _check_length(idnum)
    rdtm = _check_reg(idnum)
    rday = rdtm.strftime("%d %B %Y")
    return rday

def nth_pub(idnum: Union[str, int]) -> int:
    idnum = _check_length(idnum)
    nth = int(idnum[13:])
    return nth

def all_info(idnum: Union[str, int]) -> dict:
    kk_dict = {'NIK': idnum, 'province': province(idnum), 'city': city(idnum), 'district': district(idnum),
            'regist_datetime': regdtm(idnum), 'regist_day': regday(idnum),
            'regist_code': nth_pub(idnum)}

    return kk_dict