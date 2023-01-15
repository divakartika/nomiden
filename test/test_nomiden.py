import pandas as pd
import nomiden
from nomiden import nik
from nomiden import kk
from nomiden import reader

print(nik.province(3213034912000005))
print(nik.city(3213034912000005))
print(nik.district(3213034912000005))
print(nik.gender(3213034912000005))
print(nik.birthdate(3213034912000005))
print(nik.birthmonth(3213034912000005))
print(nik.birthyear(3213034912000005))
print(nik.birthdtm(3213034912000005))
print(nik.birthday(3213034912000005))
print(nik.age(3213034912000005))
print(nik.nthperson(3213034912000005))

print('\n')

print(kk.province('3175042901099014'))
print(kk.city(3175042901099014))
print(kk.district(3175042901099014))
print(kk.regdate(3175042901099014))
print(kk.regmonth(3175042901099014))
print(kk.regyear(3175042901099014))
print(kk.regdtm(3175042901099014))
print(kk.regday(3175042901099014))
print(kk.nthpub(3175042901099014))

df = pd.DataFrame([3213034912000005, 3175045506000006], columns=['NIK'])
df['usia'] = df['NIK'].apply(nik.age)
print(df)

nik_list = []
for i in [3213034912000005, 3175045506000006]:
    print(nik.city(i))
    nik_list.append(reader.nik(i))

nik_df = pd.DataFrame.from_dict(nik_list)
print(nik_df)

nik_dict = reader.nik(3213034912000005)
print(nik_dict)
nik_df = pd.DataFrame.from_dict([nik_dict])
print(nik_df)