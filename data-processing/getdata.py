import pandas as pd
import requests
from bs4 import BeautifulSoup

def kpp():

    # Create an URL object
    url = 'http://www.pajakita.net/p/wilayah-kerja-kantor-pelayanan-pajak.html'

    # Create object page
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    # Obtain information from tag <table>
    table = soup.find('table')

    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)

    # Create a dataframe
    kpp_df = pd.DataFrame(columns = headers)

    # Create a for loop to fill mydata
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        # length = len(kpp_df)

    #  mydata.loc[length] = row
    kpp_df = kpp_df.append(pd.Series(row, index=kpp_df.columns[:len(row)]), ignore_index=True)

    return kpp_df

kpp()