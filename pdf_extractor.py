import PyPDF2


def extract_text_from_pdf(pdf_path):
    """
    Extract text content from a PDF file.

    :param pdf_path: Path to the PDF file
    :return: Extracted text as a string
    """
    text = ""
    print("Extracting text from PDF...")
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def clean_text(text):
    """
    Clean and preprocess the extracted text.

    :param text: Raw text extracted from PDF
    :return: Cleaned text
    """
    # Remove extra whitespace and newlines
    cleaned_text = ' '.join(text.split())
    return cleaned_text
