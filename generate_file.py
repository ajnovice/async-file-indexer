import random

file_path = "file.txt"
file_lines = 10000


def generate_random_line():
    num_words = random.randint(1, 10)
    words = [str(random.randint(1, 100)) for _ in range(num_words)]
    return ' '.join(words) + '\n'


def generate_random_file():
    with open(file_path, 'w') as file:
        for i in range(file_lines):
            file.write(generate_random_line())


if __name__ == '__main__':
    generate_random_file()
    print(f"File with {file_lines} lines created at: {file_path}")
