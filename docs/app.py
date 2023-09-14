from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']

        output = predict_category(input_text)[0]
        output_title = predict_title(input_text)[0]
        output_genre = predict_genres(input_text)[0]

        confidence_list = output['confidences']
        confidence_list_title = output_title['confidences']
        confidence_list_genre = output_genre['confidences']

        labels = [elem['label'] for elem in confidence_list if elem['confidence'] >= 0.5]
        label_text = ""
        for idx, label in enumerate(labels):
            label_text = label_text + label
            if idx != len(labels)-1:
                label_text = label_text + ", "

        labels_title = [elem['label'] for elem in confidence_list_title if elem['confidence'] >= 0.5]
        label_text_title = ""
        for idx, label in enumerate(labels_title):
            label_text_title = label_text_title + label
            if idx != len(labels) - 1:
                label_text_title = label_text_title + ", "

        labels_genre = [elem['label'] for elem in confidence_list_genre]
        label_text_genre = ""
        for idx, label in enumerate(labels_genre):
            label_text_genre = label_text_genre + label
            if idx != len(labels) - 1:
                label_text_genre = label_text_genre + ", "

        return render_template("result.html", input_text=input_text, output_text=label_text,
                               output_title=label_text_title, output_genre=label_text_genre)
    else:
        return render_template("index.html")


def predict_category(input_text):
    response = requests.post("https://myte-ev-entertainment-category.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data


def predict_title(input_text):
    response = requests.post("https://myte-ev-entertainment-title.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data


def predict_genres(input_text):
    response = requests.post("https://myte-ev-entertainment-genre.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data


if __name__ == "__main__":
    app.run(debug=True)
