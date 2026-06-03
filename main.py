from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vector import retriever

model = OllamaLLM(model="gpt-oss:20b-cloud")

template = """ 
    Eres un experto respondiendo preguntas acerca de futbol y del mundial FIFA 2026.
    Aquí tienes datos sobre los equipos: {context}
    Responde a la siguiente pregunta de forma breve y en español: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model | StrOutputParser()

while True:
    question = input("Haz tu Pregunta: ")
    if question.lower() == "salir":
        break
    
    docs = retriever.invoke(question)
    context = "\n".join([doc.page_content for doc in docs])
    
    response = chain.invoke({
        "question": question,
        "context": context
    })
    print("Respuesta:", response)