import io
import asyncio

binary_stream_from_file = io.BufferedReader(
    io.BytesIO(b'Bumho Nisubire')
)
bytes = binary_stream_from_file.read(5)
print(bytes)

# # TextIOWrapper
# f = io.FileIO('E:\Projects\python projects\python-projects\data.txt')
# br = io.BufferedReader(f)
# text_stream = io.TextIOWrapper(br,'utf-8')

# StringIO
memory_text = io.StringIO('to be or not be?')
print('memory_text', memory_text)
print(memory_text.getvalue())
memory_text.close

