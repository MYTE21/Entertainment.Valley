import requests


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
