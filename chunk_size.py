CHUNK_SIZE=4096
chunk = hot.read(CHUNK_SIZE)
while chunk:
    process_chunk(chunk)
    chunk = hot.read(CHUNK_SIZE)
