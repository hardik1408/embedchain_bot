import gradio as gr
from embedchain import App
import os
from dotenv import load_dotenv

load_dotenv() 

app = App.from_config(config_path="config.yaml")

def slow_echo(message, history):
    i = 0
    if i == 0:
        initial_msg = message
        app.add(initial_msg)
        yield "I have gathered information about you, now you may ask questions."
        i = 1
    resp=app.query(message)
    answer_text = resp.split("Answer:")[1].strip()
    yield answer_text

gr.ChatInterface(
    slow_echo,
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7)
).launch()


