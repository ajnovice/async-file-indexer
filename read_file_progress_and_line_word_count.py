import asyncio
import random

lines_read = 0
total_lines_in_file = 0
chunk_size = 2000

async def process_line(line):
    global lines_read
    lines_read += 1
    words_count = len(line.split())
    await asyncio.sleep(random.randint(0, 5))
    print(f"line : {line}Words in line: {words_count}\n")

async def process_chunk(chunk):
    tasks = [process_line(line) for line in chunk]
    await asyncio.gather(*tasks)

def read_and_process_chunk(chunk):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(process_chunk(chunk))

async def read_and_process_file(filename):
    global total_lines_in_file
    with open(filename, 'r') as file:
        total_lines_in_file = sum(1 for _ in file)
    with open(filename, 'r') as file:
        while True:
            chunk = [file.readline() for _ in range(chunk_size)]
            if not any(chunk):
                break
            await asyncio.get_event_loop().run_in_executor(None, read_and_process_chunk, chunk)

async def progress_report():
    global lines_read, total_lines_in_file
    while True:
        progress = lines_read / total_lines_in_file
        print(f"Progress: {progress:.2%}")
        if progress >= 1.0:
            break
        await asyncio.sleep(1)

async def main(filename):
    tasks = [read_and_process_file(filename), progress_report()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    filename = "file.txt"
    asyncio.run(main(filename))
