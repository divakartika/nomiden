from datetime import date, datetime
import pandas as pd
# from data import regioncode as rc

rc = pd.read_csv('data/regioncode.csv')

def province(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2]
        prov = rc.loc[rc['code'] == prov_code, 'region'].item()
        return prov
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
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
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
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
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def regdate(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        rcode = idnum[6:12]
        if int(rcode[:2]) > 31:
            rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
        rdtm = datetime.strptime(rcode, "%d%m%y")
        rdate = rdtm.day
        return rdate
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def regmonth(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        rcode = idnum[6:12]
        if int(rcode[:2]) > 31:
            rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
        rdtm = datetime.strptime(rcode, "%d%m%y")
        rmonth = rdtm.month
        return rmonth
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def regyear(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        rcode = idnum[6:12]
        if int(rcode[:2]) > 31:
            rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
        rdtm = datetime.strptime(rcode, "%d%m%y")
        ryear = rdtm.year
        return ryear
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def regdtm(idnum): # registration day in datetime data type
    idnum = str(idnum)
    if len(idnum) == 16:
        rcode = idnum[6:12]
        if int(rcode[:2]) > 31:
            rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
        rdtm = datetime.strptime(rcode, "%d%m%y")
        return rdtm
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def regday(idnum): # registration day in string data type
    idnum = str(idnum)
    if len(idnum) == 16:
        rcode = idnum[6:12]
        if int(rcode[:2]) > 31:
            rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
        rdtm = datetime.strptime(rcode, "%d%m%y")
        rday = rdtm.strftime("%d %B %Y")
        return rday
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

def nthpub(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        nth = int(idnum[13:])
        return nth
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 