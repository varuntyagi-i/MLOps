from flask import Flask, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

model = pickle.load(open("modelcreation/rfcclassifier.pkl", mode="rb"))
labelencoder = pickle.load(open("modelcreation/rfclabelencoder.pkl", mode="rb"))


@app.route("/ping")
def preintmyname():
    return("hello varun")

@app.route("/predict", methods=["POST"])
def prediction():
    loan_req = request.get_json()
    loan_req = pd.DataFrame(loan_req, index=[0])

    cols = loan_req.select_dtypes("object").columns.tolist()
    for i in cols:
        loan_req[i] = labelencoder[i].transform(loan_req[i])
    
    loan_req = loan_req[["Gender","Married","ApplicantIncome","LoanAmount","Credit_History"]]
    prediction = model.predict(loan_req)
    if prediction:
        return "Accepted"
    else:
        return "Rejected"
    

if __name__ == "__main__":
    port = int(os.enviorn.get("PORT", 2350))
    app.run(host = "0.0.0.0", port = 2350)




# systemctl --user start docker-desktop
# flask --app app run
