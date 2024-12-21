from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'New project': 'This is the first app of my new project !'}


@app.post("/test")
def essai(longitude : float,
          latitude : float,
          housing_median_age : int,
          total_rooms : int,
          total_bedrooms : int,
          population : int,
          households : int,
          median_income : float,
          ocean_proximity : str):
    return longitude, latitude, housing_median_age,\
          total_rooms, total_bedrooms,population,\
          households, median_income, ocean_proximity
