from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os

Base_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(Base_DIR, 'model', 'nyctaxi.joblib'))

input_cols = ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count',
              'pickup_datetime_year','pickup_datetime_month','pickup_datetime_day','pickup_datetime_weekday',
              'pickup_datetime_hour','trip_distance','jfk_drop_distance','lga_drop_distance','ewr_drop_distance',
              'met_drop_distance','wtc_drop_distance']


class TaxiInput(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int
    pickup_datetime_year: int
    pickup_datetime_month: int
    pickup_datetime_day: int
    pickup_datetime_weekday: int
    pickup_datetime_hour: int
    trip_distance: float
    jfk_drop_distance: float
    lga_drop_distance: float
    ewr_drop_distance: float
    met_drop_distance: float
    wtc_drop_distance: float
    
    
app = FastAPI(title="NYC Taxi Fare Prediction API")

@app.get('/')
def read_root():
    return {'message':'MYC Taxi Fare Prediction API running'}

@app.post("/predict")
def predict_fare(input: TaxiInput):
    try:
        
        # coverting input to dataframe
        input_df = pd.DataFrame([input.dict()])
        
        #prediction directly
        pred = float(model.predict(input_df)[0])
        
        return {"Prediction": pred}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    