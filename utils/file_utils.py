import pdfplumber

# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""  # Handle pages with no text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")
    return text

# Function to split text into chunks based on token limit
def split_text_into_chunks(text, max_tokens=4000):
    """
    Splits the text into chunks of approximately `max_tokens` tokens.
    Assumes 1 token ≈ 4 characters or 0.75 words.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        # Approximate token count (1 token ~= 4 characters or 0.75 words)
        if len(" ".join(current_chunk)) > max_tokens * 0.75:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
