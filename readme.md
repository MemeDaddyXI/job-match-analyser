# Job Match Analyser

A Python CLI tool that analyses how well your CV matches a job description using local AI (Ollama + LLaMA 3.2).

## What it does
- Reads a job description (txt) and your CV (PDF or txt)
- Runs analysis locally — no API keys, no cost, no data leaving your machine
- Returns a match score, matched keywords, missing keywords, and a top CV tip

## How to use
1. Install [Ollama](https://ollama.com) and run `ollama pull llama3.2`
2. Install dependencies: `pip install ollama pymupdf`
3. Run: `py analyse.py`
4. Drag and drop your files when prompted

## Tech
Python · Ollama · LLaMA 3.2 · PyMuPDF