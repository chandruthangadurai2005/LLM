import streamlit as st
from main_llm import MathLLMSolver
from solver_verify import verify_equation

st.set_page_config(page_title="AI Math Solver (Ollama + SymPy)", layout="centered")
st.title("🧮 AI Math Solver (Ollama + SymPy)")

model_name = st.text_input("Ollama model name:", value="deepseek-coder:1.3b")
host = st.text_input("Ollama server URL:", value="http://localhost:11434")

operation = st.selectbox("Operation:", ["Solve", "Integrate", "Differentiate", "Simplify"])
problem = st.text_area("Enter your math problem (do NOT include the word 'Integrate'):", height=120)

if st.button("Solve"):
    if not problem.strip():
        st.warning("Please enter a problem.")
    else:
        # Debug line (temporary) to ensure operation is correct
        st.write("DEBUG Operation selected:", operation)

        solver = MathLLMSolver(model_name=model_name, host=host)
        with st.spinner("Generating reasoning from LLM..."):
            llm_answer = solver.solve(problem, operation)

        st.subheader("🧠 LLM Step-by-Step Reasoning")
        st.write(llm_answer or "No LLM output (check Ollama server).")

        st.subheader("✔️ SymPy Verification / Result")
        sym_result = verify_equation(problem, operation)   # Must pass operation
        st.success(sym_result)
        st.write(sym_result)
