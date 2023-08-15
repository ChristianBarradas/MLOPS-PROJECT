import os
import sys

from fastapi import FastAPI
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse

from .models.models import HousePricePrediction

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    return 'house predict classifier is all ready to go!'


@app.post('/predict')
def extract_name(housing_features: HousePricePrediction):
    predictor = ModelPredictor("/Users/SISTEMAS/MLOPS-PROJECT/house_price_prediction/house_price_prediction/models/neural_network_model.pkl")
    X = [housing_features.bedrooms, housing_features.bathrooms, housing_features.sqft_living, housing_features.sqft_lot, housing_features.floors, housing_features.waterfront, housing_features.view, housing_features.condition, housing_features.grade, housing_features.sqft_above, housing_features.sqft_basement, housing_features.yr_built, housing_features.yr_renovated, housing_features.lat, housing_features.long, housing_features.sqft_lot15, housing_features.sqft_living15, housing_features.month, housing_features.year]
    prediction = predictor.predict([X])
    return JSONResponse(f"Resultado predicción: {prediction}")
