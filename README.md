# NYC Taxi Fare Prediction API

**Project Overview:**
This project provides a RESTful API for predicting NYC taxi fares using a pre-trained LightGBM regression model. The API is built with **FastAPI**, allowing quick and scalable predictions for single or batch requests.

---

## Features

* Predict taxi fares based on pickup/dropoff locations, datetime, passenger count, and distances to major airports & landmarks.
* FastAPI-powered with **automatic Swagger docs** (`/docs` endpoint).
* Handles input validation using **Pydantic models**.
* Easy integration for web or mobile applications.

---

## Input Features

The model expects the following inputs:

| Feature                   | Type  | Description                     |
| ------------------------- | ----- | ------------------------------- |
| `pickup_longitude`        | float | Pickup location longitude       |
| `pickup_latitude`         | float | Pickup location latitude        |
| `dropoff_longitude`       | float | Dropoff location longitude      |
| `dropoff_latitude`        | float | Dropoff location latitude       |
| `passenger_count`         | int   | Number of passengers            |
| `pickup_datetime_year`    | int   | Pickup year                     |
| `pickup_datetime_month`   | int   | Pickup month                    |
| `pickup_datetime_day`     | int   | Pickup day                      |
| `pickup_datetime_weekday` | int   | Day of the week (1–7)           |
| `pickup_datetime_hour`    | int   | Pickup hour (0–23)              |
| `trip_distance`           | float | Distance traveled by the taxi   |
| `jfk_drop_distance`       | float | Distance to JFK airport         |
| `lga_drop_distance`       | float | Distance to LGA airport         |
| `ewr_drop_distance`       | float | Distance to EWR airport         |
| `met_drop_distance`       | float | Distance to Metropolitan Museum |
| `wtc_drop_distance`       | float | Distance to World Trade Center  |

---

## Installation

```bash
git clone <repo_url>
cd FastAPI_NYC

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

## Running the API

```bash
uvicorn app:app --reload --port 8000
```

* Access API root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Access interactive Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Example Request

**cURL single prediction:**

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "pickup_longitude": -73.985428,
  "pickup_latitude": 40.748817,
  "dropoff_longitude": -73.985428,
  "dropoff_latitude": 40.748817,
  "passenger_count": 1,
  "pickup_datetime_year": 2023,
  "pickup_datetime_month": 8,
  "pickup_datetime_day": 4,
  "pickup_datetime_weekday": 1,
  "pickup_datetime_hour": 14,
  "trip_distance": 2.5,
  "jfk_drop_distance": 20.3,
  "lga_drop_distance": 15.7,
  "ewr_drop_distance": 30.2,
  "met_drop_distance": 5.0,
  "wtc_drop_distance": 10.0
}'
```

**Response:**

```json
{
  "Prediction": 15.026287725871494
}
```

---

## Project Structure

```
FastAPI_NYC/
├── app.py                  # FastAPI application
├── model/
│   └── nyctaxi.joblib      # Pre-trained LightGBM model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── __pycache__/            # Python cache files
```

---

## Notes

* The model currently does **not use feature scaling or encoding**. Ensure inputs are provided in raw format.
* Consider adding **input validation** to avoid unrealistic predictions (e.g., 100 passengers).
* Can be easily extended to batch predictions, logging, or deployed via Docker.
