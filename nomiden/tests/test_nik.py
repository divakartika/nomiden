import pandas as pd
import unittest
from datetime import datetime
from nomiden import nik

int_idnums = [1101010101000000, 1101014101000000]
str_idnums = ["1101010101000000", "1101014101000000"]

class TestNIK(unittest.TestCase):
    def test_invalid_idnum_error(self):
        idnum_15 = 101014101000000
        idnum_17 = 11101014101000000

        with self.assertRaises(ValueError):
            nik._check_length(idnum_15)
            nik._check_length(idnum_17)

    def test_valid_idnum(self):
        for idnum in int_idnums:
            valid_idnum = nik._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)
        for idnum in str_idnums:
            valid_idnum = nik._check_length(idnum)
            self.assertEqual(len(valid_idnum), 16)

    def test_nik_province(self):
        for idnum in int_idnums:
            prov = nik.province(idnum)
            self.assertIsInstance(prov, str)
        for idnum in str_idnums:
            prov = nik.province(idnum)
            self.assertIsInstance(prov, str)

    def test_nik_city(self):
        for idnum in int_idnums:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)
        for idnum in str_idnums:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)

    def test_nik_city(self):
        for idnum in int_idnums:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)
        for idnum in str_idnums:
            city = nik.city(idnum)
            self.assertIsInstance(city, str)

    def test_nik_district(self):
        for idnum in int_idnums:
            dist = nik.district(idnum)
            self.assertIsInstance(dist, str)
        for idnum in str_idnums:
            dist = nik.district(idnum)
            self.assertIsInstance(dist, str)

    def test_nik_gender(self):
        for idnum in int_idnums:
            gend = nik.gender(idnum)
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
        for idnum in str_idnums:
            gend = nik.gender(idnum)
            self.assertIsInstance(gend, str)
            self.assertIn(gend, {'Male', 'Female'})
    
    def test_nik_birthdate(self):
        for idnum in int_idnums:
            bdate = nik.birthdate(idnum)
            self.assertIsInstance(bdate, int)
        for idnum in str_idnums:
            bdate = nik.birthdate(idnum)
            self.assertIsInstance(bdate, int)

    def test_nik_birthmonth(self):
        for idnum in int_idnums:
            bmonth = nik.birthmonth(idnum)
            self.assertIsInstance(bmonth, int)
        for idnum in str_idnums:
            bmonth = nik.birthmonth(idnum)
            self.assertIsInstance(bmonth, int)

    def test_nik_birthyear(self):
        for idnum in int_idnums:
            byear = nik.birthyear(idnum)
            self.assertIsInstance(byear, int)
        for idnum in str_idnums:
            byear = nik.birthyear(idnum)
            self.assertIsInstance(byear, int)

    def test_nik_birthdtm(self):
        for idnum in int_idnums:
            bdtm = nik.birthdtm(idnum)
            self.assertIsInstance(bdtm, datetime)
        for idnum in str_idnums:
            bdtm = nik.birthdtm(idnum)
            self.assertIsInstance(bdtm, datetime)

    def test_nik_birthday(self):
        for idnum in int_idnums:
            bday = nik.birthday(idnum)
            self.assertIsInstance(bday, str)
        for idnum in str_idnums:
            bday = nik.birthday(idnum)
            self.assertIsInstance(bday, str)

    def test_nik_age(self):
        for idnum in int_idnums:
            age = nik.age(idnum)
            self.assertIsInstance(age, int)
        for idnum in str_idnums:
            age = nik.age(idnum)
            self.assertIsInstance(age, int)

    def test_nik_nthperson(self):
        for idnum in int_idnums:
            nth = nik.nthperson(idnum)
            self.assertIsInstance(nth, int)
        for idnum in str_idnums:
            nth = nik.nthperson(idnum)
            self.assertIsInstance(nth, int)

    def test_nik_nikreader(self):
        for idnum in int_idnums:
            nik_dict = nik.nikreader(idnum)
            self.assertIsInstance(nik_dict, dict)
        for idnum in str_idnums:
            nik_dict = nik.nikreader(idnum)
            self.assertIsInstance(nik_dict, dict)

if __name__ == '__main__':
    unittest.main()