# Pollen Level Checker

This project is designed to retrieve and monitor the pollen levels in various cities. It leverages the power of Large Language Models (LLM) and Langchain to extract data from specified website.

The Pollen Level Checker is particularly useful for individuals with allergies, as it provides updates on pollen levels, allowing users to take necessary precautions and plan their activities accordingly.

## Features
* Retrieves real-time pollen levels from specified website.
* Utilizes Large Language Models (LLM) and Langchain for accurate data extraction.
* Easy to set up and run locally.
* Can be customized to monitor pollen levels in different cities.
* Follow the instructions in the 'Prerequisite' and 'Running the app' sections to set up and run the Pollen Level Checker.

## Prerequisite
### Local LLM using Ollama
1. Download the native installer of Ollama from https://ollama.com/, or
    install with homebrew if you want (also useful if you don't have admin right on your laptop).
    ```
    brew install ollama
    ```
2. Download a model (e.g. llama3)
    ```
    ollama pull ollama
    ```
### install dependencies with virtualenv
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the app
1. Setup the website URL
    ```
    cp .env.sample .env
    ```
    Then update the URL in `.env`.
2. Test it
    ```
    python main.py
    ```