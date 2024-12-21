# Models
from sklearn.ensemble import RandomForestRegressor

# Saving/loading models
import joblib

def get_model():
    '''
    Reloading the saved model
    '''
    final_model_reloaded = joblib.load("data/processed_data/my_california_housing_model.pkl")
    print("✅ model has been instantiated")
    return final_model_reloaded
