def chunk_text(text: str):
    return [line.strip() for line in text.split("\n") if line.strip()]
