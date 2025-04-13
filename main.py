import re
import time

import requests
from collections import Counter


def normalize_text(text):
    words = re.findall(r"\b\w+'\w+|\w+\b", text)
    return words


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    start = time.perf_counter()

    with open(words_file, 'r') as file:
        words_to_count = [line.strip() for line in file]

    text = requests.get(url).text
    words = normalize_text(text)
    counter = Counter(words)
    frequencies = {word: counter.get(word, 0) for word in words_to_count}

    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.6f} секунд")

    print(frequencies)
    print(counter.total())

if __name__ == "__main__":
    main()
