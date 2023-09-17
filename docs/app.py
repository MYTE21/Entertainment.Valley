from flask import Flask, render_template, request
from utilities import predict, result

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form['my_text']

        predicted_categories = predict.predict_category(input_text)[0]
        category = result.get_category(predicted_categories)

        predicted_titles = predict.predict_title(input_text)[0]
        titles = result.get_titles(predicted_titles)

        predicted_genres = predict.predict_genres(input_text)[0]
        genres = result.get_genres(predicted_genres)

        return render_template("index.html", input_text=input_text, category=category,
                               titles=titles, genres=genres)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
