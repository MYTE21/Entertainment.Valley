import requests


def predict_title(input_text):
    response = requests.post("https://myte-ev-entertainment-title.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data


text = "The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic."
print(predict_title(text))
