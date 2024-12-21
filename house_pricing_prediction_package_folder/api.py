# Import libraries
from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd

# Import from api py files
from house_pricing_prediction_package_folder.api_functions.data_api import create_X
from house_pricing_prediction_package_folder.api_functions.model_api import get_model_api

# Instantiate api
app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'New project': 'This is the first app of my new project !'}

@app.post("/predict")
def predict_func(longitude : float,
          latitude : float,
          housing_median_age : int,
          total_rooms : int,
          total_bedrooms : int,
          population : int,
          households : int,
          median_income : float,
          ocean_proximity : str):
    # Create X (features)
    X = create_X(longitude, latitude, housing_median_age,
          total_rooms, total_bedrooms,population,households,
          median_income, ocean_proximity)

    # Get the model to use
    final_model = get_model_api()

    # Predict
    prediction = final_model.predict(X)
    print("✅ predictions has been calculated")
    prediction = [round(pred, 2) for pred in prediction]

    # Create a prediction dataframe
    predictions_df = pd.DataFrame({"prediction" : prediction})

    # Concatenate X and prediction as result
    result = pd.concat([X,predictions_df], axis = 1)

    result.to_json(path_or_buf = "data/processed_data/prediction_response.json")

    file_path = "data/processed_data/prediction_response.json"  # Path to your JSON file
    return FileResponse(file_path, media_type="application/json", filename="prediction_response.json")
