import pathlib
import pandas as pd
import geopandas as gpd


def load_data(index: bool = False) -> pd.DataFrame:
    """
    Function for loading and cleaning data in a usable format

    Parameters:
    -----------
    index: boolean indicating whether to load data with a specified index column

    Returns:
    --------
    A pandas DataFrame object containing cleaned data
    """
    data = load_raw_data(index=index)

    data[['earlier_date', 'later_date']] = data['Commissioning date'].str.split('/', 1, expand = True)
    data.earlier_date.fillna(data['Commissioning date'], inplace=True)
    data = data.drop(['Commissioning date', 'later_date'], axis = 1)
    data = data.rename(columns = {'earlier_date' : 'Commissioning date'})
    data['Commissioning date'] = pd.to_numeric(data['Commissioning date'])

    return data


def load_raw_data(index: bool = True) -> pd.DataFrame:
    """
    Function for loading raw data 

    Parameters:
    -----------
    index: boolean indicating whether to load data with indexed column

    Returns:
    --------
    A pandas DataFrame object containing raw data
    """
    root_dir = pathlib.Path(__file__).parent.parent
    file_path = root_dir.joinpath("data/WindTurbineDatabase.xlsx")
    if index:
        return pd.read_excel(file_path, index_col = 0)
    return pd.read_excel(file_path)


def load_geo_data() -> gpd.GeoDataFrame:
    """
    Function for loading geographical data for rendering map

    Returns:
    --------
    A geopandas GeoDataFrame object containing Canadian map data
    """
    root_dir = pathlib.Path(__file__).parent.parent
    file_path = root_dir.joinpath("data/canada.geojson")
    return gpd.read_file(file_path)