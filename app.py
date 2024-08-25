from qroq import Groq
import os
os.environ['GROQ_API_KEY'] = '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'
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Explain the importance of fast language models"}
    ],
    model="llama3-70b-8192",
    temperature=0
)

print(chat_completion.choices[0].message.content)