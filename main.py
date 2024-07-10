import argparse
import os
from pdf_extractor import extract_text_from_pdf, clean_text
from gpt_summarizer import summarize_text
from utils import load_api_key


def main():
    parser = argparse.ArgumentParser(description="Summarize a scientific article PDF using GPT API")
    parser.add_argument("-f", "--file", required=True, help="Path to the PDF file")
    args = parser.parse_args()

    # Check if the file exists
    if not os.path.isfile(args.file):
        print(f"Error: The file '{args.file}' does not exist.")
        return

    # Extract text from PDF
    raw_text = extract_text_from_pdf(args.file)
    cleaned_text = clean_text(raw_text)

    # Load API key
    api_key = load_api_key()

    # Summarize text
    summary = summarize_text(api_key, cleaned_text)

    # Create 'data' directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Generate output file path
    output_filename = os.path.splitext(os.path.basename(args.file))[0] + '_summary.md'
    output_path = os.path.join('data', output_filename)

    # Write summary to file
    with open(output_path, 'w') as file:
        file.write(summary.content)

    print(f"Summary has been saved to: {output_path}")


if __name__ == "__main__":
    main()
