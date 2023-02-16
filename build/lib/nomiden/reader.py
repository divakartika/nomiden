from typing import Union

from nomiden import nik
from nomiden import kk

class NIK:
    """
    A class to represent personal ID number, NIK (Nomor Induk Kependudukan).

    ...

    Parameters
    ----------
        idnum : int or str
            personal ID number (NIK)

    Attributes
    ----------
    province : str
        province of the NIK holder
    city : str
        city of the NIK holder
    gender : str
        gender of the NIK holder
    birthdate : int, 1 to 31
        date of birth (date of the month) of the NIK holder
    birthmonth : int, 1 to 12
        month of birth of the NIK holder
    birthyear : int
        year of birth of the NIK holder
    birthdtm : datetime64
        complete day of birth (datetime64 format) of the NIK holder
    birthday : str
        complete day of birth (str format) of the NIK holder
    age : int
        age of the NIK holder
    nth_person : int
        NIK registration order number
    all_info : dict
        complete information of the NIK holder in dict format
    """
    def __init__(self, idnum: Union[str, int]):
        """
        Constructs all the necessary attributes for the NIK object.

        Parameters
        ----------
            idnum : int or str
                ID number (NIK)
        """
        self.province = nik.province(idnum)
        self.city = nik.city(idnum)
        self.district = nik.district(idnum)
        self.gender = nik.gender(idnum)
        self.birthdate = nik.birthdate(idnum)
        self.birthmonth = nik.birthmonth(idnum)
        self.birthyear = nik.birthyear(idnum)
        self.birthdtm = nik.birthdtm(idnum)
        self.birthday = nik.birthday(idnum)
        self.age = nik.age(idnum)
        self.nth_person = nik.nth_person(idnum)
        self.all_info = nik.all_info(idnum)

class KK:
    """
    A class to represent family ID number, KK (Kartu Keluarga).

    ...

    Parameters
    ----------
        idnum : int or str
            family ID number (KK)

    Attributes
    ----------
    province : str
        province of the family based on KK registered
    city : str
        city of the family based on KK registered
    regdate : int, 1 to 31
        date of registration (date of the month) of KK
    regmonth : int, 1 to 12
        month of registration of KK
    regyear : int
        year of registration of KK
    regdtm : datetime64
        complete day of registration (datetime64 format) of KK
    regday : str
        complete day of registration (str format) of KK
    nth_pub : int
        KK registration order number
    all_info : dict
        complete information of KK in dict format
    """
    def __init__(self, idnum: Union[str, int]):
        """
        Constructs all the necessary attributes for the KK object.

        Parameters
        ----------
            idnum : int or str
                family ID number (KK)
        """
        self.province = kk.province(idnum)
        self.city = kk.city(idnum)
        self.district = kk.district(idnum)
        self.regdate = kk.regdate(idnum)
        self.regmonth = kk.regmonth(idnum)
        self.regyear = kk.regyear(idnum)
        self.regdtm = kk.regdtm(idnum)
        self.regday = kk.regday(idnum)
        self.nth_pub = kk.nth_pub(idnum)
        self.all_info = kk.all_info(idnum)