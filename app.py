import pickle
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

binary_map   = {"yes": 1, "no": 0}
furnish_map  = {"furnished": 0, "semi-furnished": 1, "unfurnished": 2}

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_df = pd.DataFrame([{
        "area"             : int(data["area"]),
        "bedrooms"         : int(data["bedrooms"]),
        "bathrooms"        : int(data["bathrooms"]),
        "stories"          : int(data["stories"]),
        "mainroad"         : binary_map[data["mainroad"]],
        "guestroom"        : binary_map[data["guestroom"]],
        "basement"         : binary_map[data["basement"]],
        "hotwaterheating"  : binary_map[data["hotwaterheating"]],
        "airconditioning"  : binary_map[data["airconditioning"]],
        "parking"          : int(data["parking"]),
        "prefarea"         : binary_map[data["prefarea"]],
        "furnishingstatus" : furnish_map[data["furnishingstatus"]],
    }])

    price = round(float(model.predict(input_df)[0]), 2)
    return jsonify({"predicted_price": price})

if __name__ == "__main__":
    app.run(debug=True)
