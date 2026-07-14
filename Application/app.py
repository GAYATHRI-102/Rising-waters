from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("floods.save")
scaler = joblib.load("transform.save")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    cloud_cover = float(request.form["cloud_cover"])
    annual = float(request.form["annual"])
    jan_feb = float(request.form["jan_feb"])
    mar_may = float(request.form["mar_may"])
    jun_sep = float(request.form["jun_sep"])

    if cloud_cover < 0 or cloud_cover > 100:
        return render_template(
            "index.html",
            error="Cloud Cover must be between 0 and 100%."
        )

    features = np.array([[cloud_cover,
                          annual,
                          jan_feb,
                          mar_may,
                          jun_sep]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    if prediction[0] == 1:
        return render_template("chance.html")
    else:
        return render_template("no_chance.html")


if __name__ == "__main__":
    app.run(debug=True)