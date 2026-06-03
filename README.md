# RAG sobre el Mundial FIFA 2026

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) cuyo conocimiento se basa en un archivo CSV con información del Mundial FIFA 2026.

## Modelo usado

Por defecto se utiliza **Ollama** con el modelo `gpt-oss:20b-cloud` para acelerar la generación de respuestas.  
Puedes cambiar el modelo editando el archivo `main.py` y sustituyéndolo por el que prefieras.

## Requisitos previos

- Python 3.8+
- Ollama instalado y ejecutándose (con el modelo elegido descargado)

## Instalación y ejecución

Sigue estos pasos para poner en marcha el proyecto:

1. **Crear un entorno virtual**
   ```bash
   python -m venv env
   
2. Activar el entorno virtual
    En Windows:
    env\Scripts\activate
   
   En Linux/Mac:
    source env/bin/activate
   
3.Instalar las dependencias
    pip install -r requirements.txt

4.Ejecutar la aplicación
Abre tu IDE (por ejemplo, Visual Studio Code) o terminal, y corre:
    python main.py
