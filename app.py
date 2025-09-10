from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import model, MODEL_VERSION, predict_output
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse

app = FastAPI()
    
@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get('/health')
def health_check():
    return {
        "status": "ok",
        "model_version": MODEL_VERSION,
        "model_status": "loaded" if model else "not loaded"
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:

        prediction = predict_output(user_input)

        return JSONResponse(
            status_code=200,
            content={  
                    "predicted_category": prediction   
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )



