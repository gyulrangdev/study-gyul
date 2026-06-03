import os
from datasets import load_dataset

os.environ["OPENAI_API_KEY"] = ""

from llama_index.core import VectorStoreIndex, Document
dataset = load_dataset("klue", "mrc", split="train")
dataset[0]
text_list = dataset[:100]['context']
documents = [Document(text=text) for text in text_list]
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("당신의 질문을 여기에 입력하세요")

print(response)
