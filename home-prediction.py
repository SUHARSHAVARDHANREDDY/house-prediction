from flask import Flask, request, render_template_string
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

X = np.array([
    [1000,2,1,1,1],
    [1200,2,2,1,1],
    [1500,3,2,1,1],
    [1800,3,2,1,1],
    [2000,3,3,1,1],
    [2200,4,3,2,1],
    [2500,4,3,2,1],
    [2800,4,4,2,1],
    [3000,5,4,2,1],
    [3500,5,5,2,1]
])
y = np.array([30,35,45,52,60,68,78,90,105,125])

model = LinearRegression()
model.fit(X, y)
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>House Price Prediction</title>

<style>

body{
margin:0;
padding:0;
font-family:Arial;
background:linear-gradient(135deg,#3498db,#2ecc71);
}

.container{

width:420px;
margin:60px auto;
background:white;
padding:30px;
border-radius:15px;
box-shadow:0 0 20px rgba(0,0,0,.3);

}

h1{

text-align:center;
color:light blue;

}

input{

width:100%;
padding:12px;
margin:10px 0;
border:1px solid gray;
border-radius:5px;
font-size:16px;

}

button{

width:100%;
padding:12px;
font-size:18px;
background:#27ae60;
color:light blue;
border:none;
border-radius:5px;
cursor:pointer;

}

button:hover{

background:#219150;

}

.result{

margin-top:20px;
text-align:center;
font-size:24px;
font-weight:bold;
color:#e74c3c;

}

.footer{

text-align:center;
margin-top:20px;
color:gray;

}

</style>

</head>

<body>

<div class="container">

<h1>🏠 House Price Prediction</h1>

<form method="POST">

<input type="number" name="area"
placeholder="Area (sq.ft)" required>

<input type="number" name="bedrooms"
placeholder="Bedrooms" required>

<input type="number" name="bathrooms"
placeholder="Bathrooms" required>

<input type="number" name="hall"
placeholder="Hall" required>

<input type="number" name="kitchen"
placeholder="Kitchen" required>

<button type="submit">
Predict Price
</button>

</form>

{% if prediction %}

<div class="result">

Predicted Price<br>

₹ {{prediction}} Lakhs

</div>

{% endif %}

<div class="footer">

Developed using Flask + Machine Learning

</div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET","POST"])

def home():

    prediction = None

    if request.method=="POST":

        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        hall = int(request.form["hall"])
        kitchen= int(request.form["kitchen"])

        price = model.predict([[area,bedrooms,bathrooms,hall,kitchen]])[0]

        prediction = round(price,2)

    return render_template_string(HTML, prediction=prediction)


if __name__=="__main__":
    app.run(debug=True)