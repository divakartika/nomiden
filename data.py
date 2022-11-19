import pandas as pd

try:
    filepath = 'https://raw.githubusercontent.com/kodewilayah/permendagri-72-2019/main/dist/base.csv'
    regioncode = pd.read_csv(filepath, header=None)
    regioncode.columns = ['code', 'region']
except:
    try:
        filepath = 'data-input/base.csv'
        regioncode = pd.read_csv(filepath, header=None)
        regioncode.columns = ['code', 'region']
    except:
        raise