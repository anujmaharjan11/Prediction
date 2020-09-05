"""Application entrypoint"""
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("predict.html")


@app.route("/predictor", methods=["POST"])
def predict():
    """Main predict function."""
    Id = request.form["s_id"]
    assignment = request.form["assignment"]
    attendance = request.form["attendance"]
    first = request.form["third"]
    gender = request.form["first"]
    second = request.form["second"]
    third = request.form["gender"]

    fields = [Id, gender, assignment, attendance, first, second, third]

    if not None in fields:
        # Datapreprocessing Convert the values to float, int
        Id = int(Id)
        assignment = int(assignment)
        attendance = int(attendance)
        first = float(first)
        second = float(second)
        third = float(third)
        gender = int(gender)

        result = [Id, assignment, attendance, first, second, third, gender]

        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)

        final = model.predict([result])[0]

        return render_template("result.html", result = final)
