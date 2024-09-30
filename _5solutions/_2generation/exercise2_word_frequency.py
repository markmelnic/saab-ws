import os
import string
from collections import Counter

def analyze_word_frequency(directory):
    word_counts = Counter()
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                # Remove punctuation
                text = text.translate(str.maketrans('', '', string.punctuation))
                words = text.split()
                word_counts.update(words)
    return dict(word_counts)

# Example usage
if __name__ == '__main__':
    directory = 'code_generation/test_texts'
    frequencies = analyze_word_frequency(directory)
    for word, count in frequencies.items():
        print(f"{word}: {count}")
