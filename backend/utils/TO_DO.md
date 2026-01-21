# Primeiro

1. ambiente virtual, variaveis de ambiente, levantamento de requisitos - check

2. Documentação - check

3. criar base de dados - check
    . modelos de dados com SQLAlchemy - check
    . criar instancia da base de dados - check
    . criar schemas - check

4. configurar modelo(s) de llm
    . gemini 1.5 flash

5. Tasks
    5.1. research {theme input}
    5.2. analysis
    5.3. draft
    5.4. edit
    5.5. write final output

6. Agents
    6.1. researcher
    6.2. Analyst
    6.3. draft
    6.4. edit
    6.5. writer


Here is the summary and the plan to get this working in an hour.
1. What has been done so far

Infrastructure Ready: You have a professional Flask factory setup with Blueprints, CORS, and SQLAlchemy. 

API Documentation Ready: Flasgger is configured, meaning as soon as we write the logic, you can test it via a browser UI (/apidocs/).

Data Models Defined: You have already thought ahead about the database schema (Themes, Drafts, Articles).

Environment Ready: You have identified the need for .env and requirements.txt.

2. What each function does (in your current files)

create_app() (app.py): The heart of your project. It initializes the database, sets up the documentation (Swagger), and connects your different "Blueprints" (routes).

generate_article() (app.py): Currently a placeholder route. It doesn't do anything yet, but it's where the user input will trigger the AI.

researcher_agent (main.py): A draft of a class. Currently, it's just a placeholder and doesn't actually call Gemini.

pipeline() (main.py): Note: This part is currently incorrect. transformers.pipeline is for downloading and running models on your own computer. Gemini is an API-based model and cannot be loaded via pipeline. (!!)

3. Steps missing to complete the 1-hour assignment

Fix Model Loading: Replace the transformers code with langchain-google-genai for Gemini.
Create the "Chain": Use LangChain to connect a Prompt (Instructions) to the Model.

Bridge the Gap: Connect your Flask route in app.py to the logic in main.py.


# Futuramente

You’ll also need to install your preferred machine learning framework.

PyTorch and TensorFlow are two of the most popular open-source frameworks for deep learning.

PyTorch was developed by Facebook’s AI Research lab (FAIR) and released in 2016. It has gained immense popularity due to its ease of use and flexibility.

TensorFlow was developed by the Google Brain team and open-sourced in 2015. It’s one of the oldest and most widely adopted frameworks for building deep learning models.

Install PyTorch:

pip install torch

(Optional) For GPU acceleration, install the appropriate CUDA drivers. Simply follow the instructions on the NVIDIA website https://developer.nvidia.com/cuda-downloads

CUDA is a parallel computing platform and application programming interface (API) model created by NVIDIA specifically for its line of GPUs (Graphics Processing Units). It allows developers to utilize NVIDIA GPU hardware for general-purpose processing (GPGPU), extending beyond the traditional use in graphics and enabling significant acceleration of computational tasks in areas like machine learning, scientific computing, and data analysis.