from transformers import pipeline

# Load text generation model
generator = pipeline("text-generation", model="gpt2")

def generate_creative_text(caption):

    # Prompt that starts the story
    prompt = f"""
Expand the following image caption into a detailed and vivid 250-word scene description.

Caption: {caption}

Description:
"""

    result = generator(
        prompt,
        max_new_tokens=300,       # generate around 250 words
        min_new_tokens=220,       # ensure long output
        temperature=0.8,          # creativity
        top_p=0.9,
        top_k=50,
        repetition_penalty=1.3,   # avoid repeating phrases
        no_repeat_ngram_size=3,
        do_sample=True,
        pad_token_id=50256
    )

    generated_text = result[0]["generated_text"]

    # Remove the prompt from output
    final_text = generated_text.replace(prompt, "").strip()

    return final_text


# Example
caption = "A small boy flying a kite in a green field"
output = generate_creative_text(caption)

print(output)