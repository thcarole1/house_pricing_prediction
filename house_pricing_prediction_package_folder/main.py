# Import from .py files
from ml_logic.data import load_housing_data
from ml_logic.preprocessor import create_x_y
from ml_logic.model import get_model

# Import libraries
from sklearn.pipeline import make_pipeline

def predict_house_price(number):
    # Retrieve housing data
    housing = load_housing_data()

    # Extract a specific number of rows
    housing_sample = housing.sample(number)

    # Create X (features) and y (target)
    X, y = create_x_y(housing_sample)

    # Get the model to use
    final_model = get_model()

    # Predict
    predictions = final_model.predict(X)
    predictions = [round(prediction, 2) for prediction in predictions]
    print(predictions)

if __name__ == '__main__':
    try:
       predict_house_price(2)

    except:
        import sys
        import traceback
        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
