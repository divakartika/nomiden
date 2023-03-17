import pandas as pd
import unittest
from datetime import datetime
from nomiden import reader

int_idnums = [1101016401640000, 1101014101000000]
str_idnums = ["1101016401640000", "1101014101000000"]
df_idnums = pd.DataFrame({"idnum": str_idnums})

class TestNIKReader(unittest.TestCase):
    def test_invalid_idnum_error(self):
        idnum_15 = 101014101000000
        idnum_17 = 11101014101000000

        with self.assertRaises(ValueError):
            reader.NIK(idnum_15)
            reader.NIK(idnum_17)

    def test_nik_province(self):
        for idnum in int_idnums:
            prov = reader.NIK(idnum).province
            self.assertIsInstance(prov, str)
        for idnum in str_idnums:
            prov = reader.NIK(idnum).province
            self.assertIsInstance(prov, str)
        prov_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).province)
        self.assertIsInstance(prov_series, pd.Series)

    def test_nik_city(self):
        for idnum in int_idnums:
            city = reader.NIK(idnum).city
            self.assertIsInstance(city, str)
        for idnum in str_idnums:
            city = reader.NIK(idnum).city
            self.assertIsInstance(city, str)
        city_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).city)
        self.assertIsInstance(city_series, pd.Series)

    def test_nik_district(self):
        for idnum in int_idnums:
            dist = reader.NIK(idnum).district
            self.assertIsInstance(dist, str)
        for idnum in str_idnums:
            dist = reader.NIK(idnum).district
            self.assertIsInstance(dist, str)
        dist_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).district)
        self.assertIsInstance(dist_series, pd.Series)

    def test_nik_gender(self):
        for idnum in int_idnums:
            gend = reader.NIK(idnum).gender
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
        for idnum in str_idnums:
            gend = reader.NIK(idnum).gender
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
        gend_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).gender)
        self.assertIsInstance(gend_series, pd.Series)
    
    def test_nik_birthdate(self):
        for idnum in int_idnums:
            bdate = reader.NIK(idnum).birthdate
            self.assertIsInstance(bdate, int)
        for idnum in str_idnums:
            bdate = reader.NIK(idnum).birthdate
            self.assertIsInstance(bdate, int)
        bdate_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).birthdate)
        self.assertIsInstance(bdate_series, pd.Series)

    def test_nik_birthmonth(self):
        for idnum in int_idnums:
            bmonth = reader.NIK(idnum).birthmonth
            self.assertIsInstance(bmonth, int)
        for idnum in str_idnums:
            bmonth = reader.NIK(idnum).birthmonth
            self.assertIsInstance(bmonth, int)
        bmonth_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).birthmonth)
        self.assertIsInstance(bmonth_series, pd.Series)

    def test_nik_birthyear(self):
        for idnum in int_idnums:
            byear = reader.NIK(idnum).birthyear
            self.assertIsInstance(byear, int)
        for idnum in str_idnums:
            byear = reader.NIK(idnum).birthyear
            self.assertIsInstance(byear, int)
        byear_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).birthyear)
        self.assertIsInstance(byear_series, pd.Series)

    def test_nik_birthdtm(self):
        for idnum in int_idnums:
            bdtm = reader.NIK(idnum).birthdtm
            self.assertIsInstance(bdtm, datetime)
        for idnum in str_idnums:
            bdtm = reader.NIK(idnum).birthdtm
            self.assertIsInstance(bdtm, datetime)
        bdtm_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).birthdtm)
        self.assertIsInstance(bdtm_series, pd.Series)

    def test_nik_birthday(self):
        for idnum in int_idnums:
            bday = reader.NIK(idnum).birthday
            self.assertIsInstance(bday, str)
        for idnum in str_idnums:
            bday = reader.NIK(idnum).birthday
            self.assertIsInstance(bday, str)
        bday_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).birthday)
        self.assertIsInstance(bday_series, pd.Series)

    def test_nik_age(self):
        for idnum in int_idnums:
            age = reader.NIK(idnum).age
            self.assertIsInstance(age, int)
        for idnum in str_idnums:
            age = reader.NIK(idnum).age
            self.assertIsInstance(age, int)
        age_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).age)
        self.assertIsInstance(age_series, pd.Series)

    def test_nik_nth_person(self):
        for idnum in int_idnums:
            nth = reader.NIK(idnum).nth_person
            self.assertIsInstance(nth, int)
        for idnum in str_idnums:
            nth = reader.NIK(idnum).nth_person
            self.assertIsInstance(nth, int)
        nth_series = df_idnums['idnum'].apply(lambda x: reader.NIK(x).nth_person)
        self.assertIsInstance(nth_series, pd.Series)

    def test_nik_all_info(self):
        for idnum in int_idnums:
            nik_dict = reader.NIK(idnum).all_info
            self.assertIsInstance(nik_dict, dict)
        for idnum in str_idnums:
            nik_dict = reader.NIK(idnum).all_info
            self.assertIsInstance(nik_dict, dict)

class TestKKReader(unittest.TestCase):
    def test_invalid_idnum_error(self):
        idnum_15 = 101014101000000
        idnum_17 = 11101014101000000

        with self.assertRaises(ValueError):
            reader.KK(idnum_15)
            reader.KK(idnum_17)

    def test_kk_province(self):
        for idnum in int_idnums:
            prov = reader.KK(idnum).province
            self.assertIsInstance(prov, str)
        for idnum in str_idnums:
            prov = reader.KK(idnum).province
            self.assertIsInstance(prov, str)
        prov_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).province)
        self.assertIsInstance(prov_series, pd.Series)

    def test_kk_city(self):
        for idnum in int_idnums:
            city = reader.KK(idnum).city
            self.assertIsInstance(city, str)
        for idnum in str_idnums:
            city = reader.KK(idnum).city
            self.assertIsInstance(city, str)
        city_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).city)
        self.assertIsInstance(city_series, pd.Series)

    def test_kk_district(self):
        for idnum in int_idnums:
            dist = reader.KK(idnum).district
            self.assertIsInstance(dist, str)
        for idnum in str_idnums:
            dist = reader.KK(idnum).district
            self.assertIsInstance(dist, str)
        dist_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).district)
        self.assertIsInstance(dist_series, pd.Series)
    
    def test_kk_regdate(self):
        for idnum in int_idnums:
            bdate = reader.KK(idnum).regdate
            self.assertIsInstance(bdate, int)
        for idnum in str_idnums:
            bdate = reader.KK(idnum).regdate
            self.assertIsInstance(bdate, int)
        rdate_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).regdate)
        self.assertIsInstance(rdate_series, pd.Series)

    def test_kk_regmonth(self):
        for idnum in int_idnums:
            bmonth = reader.KK(idnum).regmonth
            self.assertIsInstance(bmonth, int)
        for idnum in str_idnums:
            bmonth = reader.KK(idnum).regmonth
            self.assertIsInstance(bmonth, int)
        rmonth_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).regmonth)
        self.assertIsInstance(rmonth_series, pd.Series)

    def test_kk_regyear(self):
        for idnum in int_idnums:
            byear = reader.KK(idnum).regyear
            self.assertIsInstance(byear, int)
        for idnum in str_idnums:
            byear = reader.KK(idnum).regyear
            self.assertIsInstance(byear, int)
        ryear_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).regyear)
        self.assertIsInstance(ryear_series, pd.Series)

    def test_kk_regdtm(self):
        for idnum in int_idnums:
            bdtm = reader.KK(idnum).regdtm
            self.assertIsInstance(bdtm, datetime)
        for idnum in str_idnums:
            bdtm = reader.KK(idnum).regdtm
            self.assertIsInstance(bdtm, datetime)
        rdtm_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).regdtm)
        self.assertIsInstance(rdtm_series, pd.Series)

    def test_kk_regday(self):
        for idnum in int_idnums:
            bday = reader.KK(idnum).regday
            self.assertIsInstance(bday, str)
        for idnum in str_idnums:
            bday = reader.KK(idnum).regday
            self.assertIsInstance(bday, str)
        rday_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).regday)
        self.assertIsInstance(rday_series, pd.Series)

    def test_kk_nth_pub(self):
        for idnum in int_idnums:
            nth = reader.KK(idnum).nth_pub
            self.assertIsInstance(nth, int)
        for idnum in str_idnums:
            nth = reader.KK(idnum).nth_pub
            self.assertIsInstance(nth, int)
        nth_series = df_idnums['idnum'].apply(lambda x: reader.KK(x).nth_pub)
        self.assertIsInstance(nth_series, pd.Series)

    def test_kk_all_info(self):
        for idnum in int_idnums:
            kk_dict = reader.KK(idnum).all_info
            self.assertIsInstance(kk_dict, dict)
        for idnum in str_idnums:
            kk_dict = reader.KK(idnum).all_info
            self.assertIsInstance(kk_dict, dict)

if __name__ == '__main__':
    unittest.main()