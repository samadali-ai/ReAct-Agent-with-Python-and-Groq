import streamlit as st
import os
import re
import httpx
from groq import Groq

# Set up the Groq API key
os.environ['GROQ_API_KEY'] = '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'
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define the Action Functions (tools)
def wikipedia(q):
    return httpx.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "search",
        "srsearch": q,
        "format": "json"
    }).json()["query"]["search"][0]["snippet"]

def calculate(operation: str) -> float:
    return eval(operation)

# Define the Agent class
class Agent:
    def __init__(self, client: Groq, system: str = "") -> None:
        self.client = client
        self.system = system
        self.messages: list = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message=""):
        if message:
            self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = client.chat.completions.create(
            model="llama3-70b-8192", messages=self.messages
        )
        return completion.choices[0].message.content

# Streamlit UI
st.title("AI-Powered Query Agent")

query = st.text_input("Enter your query:", "")

if st.button("Run"):
    if query:
        system_prompt = """
        You run in a loop of Thought, Action, PAUSE, Observation.
        At the end of the loop you output an Answer...
        """.strip()

        agent = Agent(client=client, system=system_prompt)
        tools = ["calculate", "wikipedia"]

        next_prompt = query
        max_iterations = 10
        i = 0

        result_display = []

        while i < max_iterations:
            i += 1
            result = agent(next_prompt)
            result_display.append(result)

            if "PAUSE" in result and "Action" in result:
                action = re.findall(r"Action: ([a-z_]+): (.+)", result, re.IGNORECASE)
                
                if action:  # Check if action is not empty
                    chosen_tool = action[0][0]
                    arg = action[0][1]

                    if chosen_tool in tools:
                        result_tool = eval(f"{chosen_tool}('{arg}')")
                        next_prompt = f"Observation: {result_tool}"
                    else:
                        next_prompt = "Observation: Tool not found"
                else:
                    next_prompt = "Observation: Action not recognized"

            if "Answer" in result:
                break

        st.write("Result:")
        for line in result_display:
            st.text(line)
