# from transformers import AutoTokenizer
from tool import Tool, tool

messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]

# tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
# rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# print(rendered_prompt)

@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


print(calculator.to_string())