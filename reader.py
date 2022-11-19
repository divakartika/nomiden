from datetime import date, datetime

def nik(idnum, data):
    idnum = str(idnum)
    prov_code = idnum[:2] # province
    city_code = f'{prov_code}.{idnum[2:4]}' # city
    dist_code = f'{city_code}.{idnum[4:6]}' # district / kecamatan
    birth_code = int(idnum[6:8]) # birthday date
    birth_month = idnum[8:10] # birthday month
    birth_year = idnum[10:12] # birthday year
    nth_person = int(idnum[13:]) # the nth person being recorded

    prov = data.loc[data['code'] == prov_code, 'region'].item()
    city = data.loc[data['code'] == city_code, 'region'].item()
    dist = data.loc[data['code'] == dist_code, 'region'].item()

    if birth_code >= 1 and birth_code <= 31:
        gender = "Male"
        birth_date = birth_code
    elif birth_code >= 41 and birth_code <= 71:
        gender = "Female"
        birth_date = birth_code - 40
    else:
        raise("birth_date must be between 1 to 71")

    birth_str = f'{birth_date}/{birth_month}/{birth_year}'
    birth_raw = datetime.strptime(birth_str, '%d/%m/%y')
    birthday = birth_raw.strftime("%d %B %Y")
    today = date.today()
    age = today.year - birth_raw.year - ((today.month, today.day) < (birth_raw.month, birth_raw.day))

    return prov, city, dist, gender, birthday, age, nth_person
    