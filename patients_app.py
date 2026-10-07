from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
       data = json.load(f)
    return data

@app.get("/hello")
def hello():
    return{'message': 'Hello FastAPI'}

@app.get("/")
def patients():
    return{'message': 'Patients Management system API'}

@app.get("/about")
def about():
    return{'message': 'A fully functional API for patients record management and one step solution for both doctor and patients'}

@app.get('/view')
def view():
    data = load_data()
    return data 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return{'message' :'error patient not found'}

