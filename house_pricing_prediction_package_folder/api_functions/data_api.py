import pandas as pd

def create_X(longitude : float, latitude : float, housing_median_age : int,\
          total_rooms : int, total_bedrooms : int, population : int,\
          households : int, median_income : float,ocean_proximity : str):

    dict = {"longitude" : longitude,
            "latitude" : latitude,
            "housing_median_age" : housing_median_age,
            "total_rooms" : total_rooms,
            "total_bedrooms" : total_bedrooms,
            "population" : population,
            "households" : households,
            "median_income" : median_income,
            "ocean_proximity" : ocean_proximity}
    df = pd.DataFrame(dict, index = [0])
    print("✅ X has been created")
    return df
