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

def regdate(idnum):
    idnum = str(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rdate = rdtm.day
    return rdate

def regmonth(idnum):
    idnum = str(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rmonth = rdtm.month
    return rmonth

def regyear(idnum):
    idnum = str(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    ryear = rdtm.year
    return ryear

def regdtm(idnum): # registration day in datetime data type
    idnum = str(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    return rdtm

def regstr(idnum): # registration day in string data type
    idnum = str(idnum)
    rcode = idnum[6:12]
    if int(rcode[:2]) > 31:
        rcode = rcode.replace(rcode[:2], str(int(rcode[:2]) - 40))
    rdtm = datetime.strptime(rcode, "%d%m%y")
    rstr = rdtm.strftime("%d %r %Y")
    return rstr

def nthpub(idnum):
    nth = int(idnum[13:])
    return nth