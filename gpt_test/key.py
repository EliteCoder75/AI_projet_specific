from openai import OpenAI

MODEL = "gpt-3.5-turbo"


client = OpenAI(api_key="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")

# Basic Chat

completion = client.chat.completions.create(
    model = MODEL,
    messages=[
        {"role":"system", "content":"You are a helpful assistant. Help me with my math homework"},
        {"role":"user", "content":"Hello! Can you solve 9+11?"}
    ]
)

print(f"Assistant: {completion.choices[0].message.content}")