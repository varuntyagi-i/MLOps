import pytest
from app import app 
import json 

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/ping')
    assert resp.json == {"message":"Hi Varun! Don't worry I'm working !!"}


def test_predict(client):
    test_data = {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome":5000,
    "Credit_History": 1,
    "LoanAmount": 5000
    }

    resp = client.post('predict', json = test_data)

    assert resp.status_code==200