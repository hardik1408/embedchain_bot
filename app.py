import gradio as gr
from embedchain import App
from dotenv import load_dotenv

load_dotenv() 

app = App.from_config(config_path="config.yaml")

def chat(message, history):
    i = 0
    if i == 0:
        initial_msg = message
        app.add(initial_msg)
        yield "I have gathered necessary information , now you may ask questions."
        i = 1
    resp=app.query(message)
    answer_text = resp.split("Answer:")[1].strip()
    return answer_text

gr.ChatInterface(
    chat,
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7)
).launch()


