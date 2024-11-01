from openai import OpenAI


def summarize_text(api_key, text):
    """
    Summarize the given text using GPT API.

    :param api_key: OpenAI API key
    :param text: Text to summarize
    :return: Summarized text
    """
    client = OpenAI(api_key=api_key)
    print("Summarizing text...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "You are a scientific assistant. I want you to summarize the scientific article in maximum 15 "
                        "sentences. I also want you to highlight the key points in the summary. Make sure to answer "
                        "in a Markdown format."
                        "The beginning of the output should start with the 3 main ideas of the text."
             },
            {"role": "user", "content": "Summarize the following text:\n" + text},
        ]
    )

    return response.choices[0].message
