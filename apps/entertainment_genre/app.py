import gradio as gr
import json
import torch
from transformers import AutoTokenizer
import onnxruntime as rt
import platform


if platform.system() == "Windows":
    import pathlib
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath

model_path = "entertainment-genre-quantized.onnx"

with open("genre_types_encoded.json", "r") as file:
    categories = json.load(file)

inf_session = rt.InferenceSession(model_path)
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")


def get_top_label(cat_dict, idx):
    for key, value in cat_dict.items():
        if idx == value:
            return key


def get_top_probs(cat_probs, idx):
    return cat_probs[idx]


def entertainment_genres(description):
    input_ids = tokenizer(description)['input_ids'][:512]
    probs = inf_session.run([output_name], {input_name: [input_ids]})[0]
    top_3_indices = sorted(range(len(probs[0])), key=lambda idx: probs[0][idx], reverse=True)[:3]
    cat_prob = torch.sigmoid(torch.FloatTensor(probs))[0]
    print(cat_prob)

    top_labels = []
    for i in top_3_indices:
        top_labels.append(get_top_label(categories, i))

    top_probs = []
    for i in top_3_indices:
        top_probs.append(get_top_probs(cat_prob, i))

    return dict(zip(top_labels, map(float, top_probs)))


example = [
    ["March Of Soldiers is a real time strategy single player , It is a military game based on the player's skill and "
     "the strength of his financial economy"],
    ["When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of "
     "the greatest psychological and physical tests of his ability to fight injustice."]
]


label = gr.outputs.Label(num_top_classes=3)

iface = gr.Interface(fn=entertainment_genres, inputs="text", outputs=label, examples=example)
iface.launch(inline=False)
