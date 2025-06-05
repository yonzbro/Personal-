
import aisuite as ai
import os
import tiktoken

client = ai.Client()

os.environ['GROQ_API_KEY'] = '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'

models = ['ollama:llama3.2:1b','groq:llama3-groq-70b-8192-tool-use-preview','anthropic:claude-3-5-sonnet-20241022','openai:gpt-4o','openai:gpt-4o-mini']


def crop_conversation(max_tokens, messages, next_message):
    # Initialize the tokenizer
    tokenizer = tiktoken.encoding_for_model(model_name='gpt-4o')

    # Add the next message to the conversation
    messages.append(next_message)

    # Tokenize the entire conversation and calculate tokens per message
    tokenized_messages = [(message, tokenizer.encode(message["content"])) for message in messages]
    total_tokens = sum(len(tokens) for _, tokens in tokenized_messages)

    # Crop the conversation if it exceeds the max token limit
    while total_tokens > max_tokens and tokenized_messages:
        # Find the oldest non-system message
        for i, (message, tokens) in enumerate(tokenized_messages):
            if message["role"] != "system":
                total_tokens -= len(tokens)
                tokenized_messages.pop(i)
                break

    # Extract the cropped conversation
    cropped_conversation = [message for message, _ in tokenized_messages]

    return cropped_conversation, messages, total_tokens


def basic_chatbot():
    max_tokens = 100
    messages = [
        {"role": "system", "content": "You are a helpful assistant. If not asked specifically, keep your answers short."},
    ]
    original_conversation = messages.copy()

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        next_message = {"role": "user", "content": user_input}
        cropped_conversation, original_conversation, total_tokens = crop_conversation(max_tokens, original_conversation, next_message)

        # Use the first model for the response
        model = models[1]
        response = client.chat.completions.create(
            model=model,
            messages=cropped_conversation,
            # max_tokens=30,
        )

        assistant_response = {"role": "assistant", "content": response.choices[0].message.content}
        cropped_conversation,original_conversation, total_tokens = crop_conversation(max_tokens, original_conversation, assistant_response)

        # Print the assistant's response
        print("User: ", user_input)
        print("Assistant:", assistant_response["content"])
        print("Number of token used:", total_tokens)

        # Update the messages with the cropped conversation
        messages = cropped_conversation

if __name__ == "__main__":
    basic_chatbot()