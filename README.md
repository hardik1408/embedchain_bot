# EMBEDCHAIN POWERED CHATBOT
This is a chatbot powered by embedchain.
It uses MistralAI as it's LLM, which is provided by huggingface.
It uses ChromaDB as it's vector database, which is the default vectordb in embedchain.
It contains a small UI developed with Gradio.

## RAG-Fusion
This project uses RAG-Fusion, a search methodology that aims to bridge the gap between traditional search paradigms and the multifaceted dimensions of human queries.
The system starts by generating multiple queries from a user's initial query using the model initialized before.

![rag-fusion](assets/fusion.png)

The link to the paper can be found [here](https://arxiv.org/pdf/2402.03367.pdf).

## How to run
To run the chatbot, you can simply follow the below steps:
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Run the chatbot
```bash
python3 app.py
```
4. Open the browser and go to `http://127.0.0.1:7861`
