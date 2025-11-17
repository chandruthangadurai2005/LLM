import requests
import json

class MathLLMSolver:
    def __init__(self, model_name="deepseek-coder:1.3b", host="http://localhost:11434", timeout=120):
        self.model_name = model_name
        self.host = host.rstrip("/")
        self.timeout = timeout

    def solve(self, question: str, operation="Solve") -> str:
        prompt = f"""
You are a careful math assistant. Solve the problem step-by-step using the simplest correct method.
Do not use integration by parts unless necessary. Keep the explanation short and clear.

Operation: {operation}
Problem: {question}

Answer:
"""
        url = f"{self.host}/api/generate"
        payload = {"model": self.model_name, "prompt": prompt, "stream": True}
        try:
            response = requests.post(url, json=payload, stream=True, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            return f"Error contacting Ollama: {e}\nMake sure you started the model with: ollama run <model>"

        if response.status_code != 200:
            return f"Ollama error (status {response.status_code}): {response.text}"

        final_text = ""
        for line in response.iter_lines(decode_unicode=True):
            if not line:
                continue
            try:
                j = json.loads(line)
                chunk = j.get("response") or j.get("text") or ""
                final_text += chunk
            except Exception:
                # ignore malformed chunks
                continue

        return final_text.strip()
