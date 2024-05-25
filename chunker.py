def split_text_into_chunks(text, chunk_size):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def main():
    # Load text from file or any other source
    with open('Harry_Potter_1.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Split text into chunks of 48000 words
    chunk_size = 6000
    text_chunks = split_text_into_chunks(text, chunk_size)

    # Write chunks to separate files or do any further processing
    for i, chunk in enumerate(text_chunks):
        with open(f'Chunks\chunk_{i + 1}.txt', 'w', encoding='utf-8') as file:
            file.write(chunk)

if __name__ == "__main__":
    main()