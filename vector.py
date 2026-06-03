from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("mundial_fifa_2026_equipos.csv")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Grupo"] + " " + row["Equipo"] + " " + row["Confederación"] + " " + str(row["Ranking_FIFA"]) + " " + row["Sede_Principal"],   
            metadata={"ranking": row["Ranking_FIFA"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
    vector_store = Chroma(
        collection_name="fifa_2026_equipos",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    
    vector_store.add_documents(documents=documents, ids=ids)
else:
    vector_store = Chroma(
        collection_name="fifa_2026_equipos",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 17}
)