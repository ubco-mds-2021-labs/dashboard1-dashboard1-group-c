import pandas as pd
import pathlib


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
