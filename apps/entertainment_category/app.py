import gradio as gr
import numpy as np
import json
import torch
from transformers import AutoTokenizer
import onnxruntime as rt


model_path = "entertainment-category-quantized.onnx"
with open("category.json", "r") as file:
    categories = json.load(file)["categories"]


inf_session = rt.InferenceSession(model_path)
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")


def entertainment_category(description):
    input_ids = tokenizer(description)["input_ids"][:512]
    probs = inf_session.run([output_name], {input_name: [input_ids]})[0]

    mask = np.where(probs[0] == probs.max())[0][0]
    cat = categories[mask]
    cat_prob = torch.sigmoid(torch.FloatTensor(probs))[0]

    return dict(zip(categories, map(float, cat_prob)))


with open("example.json", "r") as file:
    examples = json.load(file)["examples"]


label = gr.components.Label(num_top_classes=5)
iface = gr.Interface(fn=entertainment_category, inputs="text", outputs=label, examples=examples)
iface.launch(inline=False)
