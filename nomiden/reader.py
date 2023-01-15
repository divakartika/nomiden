from datetime import date, datetime
from data.processing import regioncode as rc

def nik(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2] # province
        city_code = f'{prov_code}.{idnum[2:4]}' # city
        dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
        birth_code = int(idnum[6:8]) # birthday date
        birth_month = idnum[8:10] # birthday month
        birth_year = idnum[10:12] # birthday year
        nth_person = int(idnum[13:]) # the nth person being recorded

        prov = rc.loc[rc['code'] == prov_code, 'region'].item()
        city = rc.loc[rc['code'] == city_code, 'region'].item()
        dist = rc.loc[rc['code'] == dist_code, 'region'].item()

        if birth_code >= 1 and birth_code <= 31:
            gender = "Male"
            birth_date = birth_code
        elif birth_code >= 41 and birth_code <= 71:
            gender = "Female"
            birth_date = birth_code - 40
        else:
            raise ValueError("Identification number (NIK) invalid, character[6:8] must be between 1 to 71")

        birth_str = f'{birth_date}/{birth_month}/{birth_year}'
        birth_dttm = datetime.strptime(birth_str, '%d/%m/%y')
        birthday = birth_dttm.strftime("%d %B %Y")
        
        today = date.today()
        age = today.year - birth_dttm.year - ((today.month, today.day) < (birth_dttm.month, birth_dttm.day))
    
        nik_dict = {'NIK': prov, 'city': city, 'district': dist,
            'gender': gender, 'birth_datetime': birth_dttm, 'birthday': birthday,
            'age': age, 'regist_code': nth_person}

    elif len(idnum) < 16:
        raise ValueError(f'Identification number (NIK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (NIK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

    return nik_dict
    
def kk(idnum):
    idnum = str(idnum)
    if len(idnum) == 16:
        prov_code = idnum[:2] # province
        city_code = f'{prov_code}.{idnum[2:4]}' # city
        dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
        reg_date = int(idnum[6:8]) # registration date
        reg_month = idnum[8:10] # birthday month
        reg_year = idnum[10:12] # birthday year
        nth_pub = int(idnum[13:]) # the nth KK being published

        prov = rc.loc[rc['code'] == prov_code, 'region'].item()
        city = rc.loc[rc['code'] == city_code, 'region'].item()
        dist = rc.loc[rc['code'] == dist_code, 'region'].item()

        reg_str = f'{reg_date}/{reg_month}/{reg_year}'
        reg_dttm = datetime.strptime(reg_str, '%d/%m/%y')
        regday = reg_dttm.strftime("%d %B %Y")

        kk_dict = {'NIK': prov, 'city': city, 'district': dist,
            'regist_datetime': reg_dttm, 'regist_day': regday,
            'regist_code': nth_pub}
    
    elif len(idnum) < 16:
        raise ValueError(f'Identification number (KK) is too short ({len(idnum)} characters), length should be 16')
    elif len(idnum) > 16:
        raise ValueError(f'Identification number (KK) is too long ({len(idnum)} characters), length should be 16')
    else:
        raise 

    return kk_dict

# TO DO: def(npwp)