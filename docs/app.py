from flask import Flask, render_template, request
import utilities.predict as predict

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['my_text']

        output = predict.predict_category(input_text)[0]
        output_title = predict.predict_title(input_text)[0]
        output_genre = predict.predict_genres(input_text)[0]

        confidence_list = output['confidences']
        confidence_list_title = output_title['confidences']
        confidence_list_genre = output_genre['confidences']

        labels = [elem['label'] for elem in confidence_list if elem['confidence']]
        label_text = str(labels[0])

        labels_title = [elem['label'] for elem in confidence_list_title if elem['confidence']]

        labels_genre = [elem['label'] for elem in confidence_list_genre]

        return render_template("index.html", input_text=input_text, output_text=label_text,
                               output_title=labels_title, output_genre=labels_genre)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
