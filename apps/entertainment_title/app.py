from fastai.text.all import *
from blurr.text.modeling.all import *
import gradio as gr


if platform.system() == "Windows":
    import pathlib
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath


model_path = "entertainment-title-stage-1.pkl"
model = load_learner(model_path)


def entertainment_title(description):
    outputs = model.blurr_summarize(description, early_stopping=True, num_beams=20, num_return_sequences=5)
    return {key: 1 for key in list(outputs[0].values())[0]}


example = [
    ["When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of "
     "the greatest psychological and physical tests of his ability to fight injustice."],
    ["The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic."]
]


labels = gr.outputs.Label(num_top_classes=5)
iface = gr.Interface(fn=entertainment_title, inputs="text", outputs=labels, examples=example)
iface.interpretation = "default"
iface.launch(inline=False)
