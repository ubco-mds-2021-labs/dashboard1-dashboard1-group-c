import pathlib
import pandas as pd
import geopandas as gpd


def load_data():
    root_dir = pathlib.Path(__file__).parent.parent
    file_path = root_dir.joinpath("data/WindTurbineDatabase.xlsx")
    data = pd.read_excel(file_path)

    data[['earlier_date', 'later_date']] = data['Commissioning date'].str.split('/', 1, expand = True)
    data.earlier_date.fillna(data['Commissioning date'], inplace=True)
    data = data.drop(['Commissioning date', 'later_date'], axis = 1)
    data = data.rename(columns = {'earlier_date' : 'Commissioning date'})
    data['Commissioning date'] = pd.to_numeric(data['Commissioning date'])

    return data

def load_raw_data():
    root_dir = pathlib.Path(__file__).parent.parent
    file_path = root_dir.joinpath("data/WindTurbineDatabase.xlsx")
    return pd.read_excel(file_path, index_col = 0)

def load_geo_data():
    # Data Wrangling 
    # wind = pd.read_excel('../data/WindTurbineDatabase.xlsx', index_col = 0)
    wind = load_raw_data()
    wind[['earlier_date', 'later_date']] = wind['Commissioning date'].str.split('/', 1, expand = True)
    wind.earlier_date.fillna(wind['Commissioning date'], inplace=True)
    wind = wind.drop(['Commissioning date', 'later_date'], axis = 1)
    wind = wind.rename(columns = {'earlier_date' : 'Commissioning date'})
    wind['Commissioning date'] = pd.to_numeric(wind['Commissioning date'])
    return wind