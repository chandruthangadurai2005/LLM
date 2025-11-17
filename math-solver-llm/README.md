🧮 AI Math Solver (Ollama + SymPy + Streamlit)

A local LLM-powered Math Solver that uses:

Ollama (runs LLMs locally)

Mistral / DeepSeek Coder models

SymPy for mathematical verification

Streamlit for the UI

Supports:

Solving equations

Integrating functions

Differentiating expressions

Simplifying expressions

LLM step-by-step reasoning

SymPy verification

Features

Accurate step-by-step reasoning from a local LLM

Verified mathematical results using SymPy

Runs completely offline (no API keys required)

Clean Streamlit interface

Solve / Integrate / Differentiate / Simplify operations

Works with any Ollama model

Getting Started
1. Fork or Download the Repository

Option A — Fork:

Click Fork on GitHub

Clone your fork:
git clone https://github.com/
<your-username>/<repo-name>.git

Option B — Download ZIP:

Click Code → Download ZIP

Extract the project

Open the folder in VS Code or Terminal

Installation
2. Install Python (3.10 or 3.11 recommended)

Download from:
https://www.python.org/downloads/

Make sure you check:
Add Python to PATH



3. Install Dependencies

pip install -r requirements.txt

This installs:

streamlit

sympy

requests

Install and Setup Ollama
4. Install Ollama

Download from:
https://ollama.com/download

Check installation:
ollama --version

5. Download a Model

Recommended (fastest – 900MB):
ollama pull deepseek-coder:1.3b

More powerful (4GB+):
ollama pull mistral:7b

6. Start the Model Server

In a new terminal window:

ollama run deepseek-coder:1.3b

This must stay open.
It starts the local API at:
http://localhost:11434

Run the Math Solver App

Back in your virtual environment terminal:

streamlit run app.py

This will open your browser at:
http://localhost:8501

How to Use

Choose the Ollama model name (example: deepseek-coder:1.3b)

Select an operation:

Solve

Integrate

Differentiate

Simplify

Type your math problem

Click Solve

The app will show:

LLM step-by-step reasoning

SymPy verified result

Example

Input:
Integrate 3*x^2

LLM Output:
Using the power rule, ∫3x² dx = x³ + C

SymPy Verification:
x^3

Project Structure

math-solver-llm/
│── app.py → Streamlit UI
│── main_llm.py → Ollama LLM request handler
│── solver_verify.py → SymPy verification logic
│── requirements.txt → Dependency list
│── README.md → Project documentation

Requirements

Python 3.10 or 3.11

Ollama installed

At least one model pulled (DeepSeek Coder, Mistral, Llama 3, etc.)

No internet needed after model download

Troubleshooting

Problem: Connection refused
Fix: Start the model
ollama run deepseek-coder:1.3b

Problem: SymPy shows [0]
Fix: Make sure the dropdown is set to “Integrate” not “Solve”

Problem: No reasoning
Fix: Model name mismatch (check using: ollama list)
