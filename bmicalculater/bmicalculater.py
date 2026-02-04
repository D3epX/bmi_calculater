from fastapi import FastAPI, Query 
from pydantic import BaseModel
#base model is used to define data models 
#cors for cross origin resource sharing and web accessibility
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)#this only for development purpose not for production and security purpose
#allowing this to access from any origin
#defining output model
class BMIoutput(BaseModel):
    bmi:float
    message:str

#define main endpoint
@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/calculate_bmi")
def claculate_bmi( 
    weight: float = Query(...,gt=20, lt=500, description="weight in kilos"),
    height: float = Query(..., gt=0.5, lt=3.0, description="height in meters")
):
    '''Calculate BMI given weight in kg and height in meters'''
    bmi=weight/(height**2)
    if bmi < 18.5:
        message="underweight eat more !"
    elif 18.5 <= bmi < 25:
        message="normal weight keep it up !"
    elif  25 <= bmi <30:
        message="overweight workout more !"
    else:
        message="obesity consult a doctor !"
        
        
    return BMIoutput(bmi=bmi, message=message)

