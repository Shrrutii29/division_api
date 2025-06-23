# to run uvicorn division:app --reload
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Message " : "Home page"}
    
class Operand(BaseModel):
    num1: float
    num2: float
    
@app.post("/division")
def divide_numbers(numbers: Operand):
    result = numbers.num1 / numbers.num2 
    return {"Result of division " : result}