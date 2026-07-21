from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
X = np.array([
    [1000, 2, 1, 1, 1],
    [1200, 2, 2, 1, 1],
    [1500, 3, 2, 1, 1],
    [1800, 3, 2, 1, 1],
    [2000, 3, 3, 1, 1],
    [2200, 4, 3, 2, 1],
    [2500, 4, 3, 2, 1],
    [2800, 4, 4, 2, 1],
    [3000, 5, 4, 2, 1],
    [3500, 5, 5, 2, 1]
])

y = np.array([30, 35, 45, 52, 60, 68, 78, 90, 105, 125])
model = LinearRegression()
model.fit(X, y)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        hall = int(request.form["hall"])
        kitchen = int(request.form["kitchen"])

        price = model.predict([[area, bedrooms, bathrooms, hall, kitchen]])[0]
        prediction = round(price, 2)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
