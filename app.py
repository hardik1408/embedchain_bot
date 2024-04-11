import gradio as gr
from embedchain import App
from dotenv import load_dotenv

load_dotenv() 

app = App.from_config(config_path="config.yaml")
app1 = App.from_config(config_path="config.yaml") 

def generate_queries(message):
    query="""You are a helpful assistant that generates multiple search queries based on a single input query.
            Generate multiple search queries related to: {message}
            OUTOUT 4 queries. Do not consider the input query as one of the output queries.
            Do not consider any history of queries."""
    
    result=app1.query(query)
    return result

def chat(message, history):
    i = 0
    if i == 0:
        initial_msg = message
        app.add(initial_msg)
        i=1
        yield "I have gathered necessary information , now you may ask questions."
        # i = 1
    
    new_message = generate_queries(message)
    resp=app.query(new_message)
    answer_text = resp.split("Answer:")[1].strip()
    yield answer_text

gr.ChatInterface(
    chat,
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7)
).launch()


