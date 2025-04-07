from urllib.request import urlopen
import time

starttime = time.time()
'''
-> pick 5 books
read 4 of the 5
write each of the 4 into a sep file
5th book title keep in mind but don't read/write

try-ex:
read num of words of the story only
find the frequency of each word in the file
num of pars
num sentences
len of smallest & longest word
most common vowel
average usage of punc 
'''

import random

book_titles = [
    "Alice's Adventures in Wonderland",
    "Frankenstein",
    "Pride and Prejudice",
    "The Adventures of Sherlock Holmes",
    "Moby Dick"
]

indices = [1,2,3,4,5]
selected_indices = random.sample(indices, 4)
excluded_index = list(set(indices) - set(selected_indices))[0]
excluded_book = book_titles[excluded_index]

print(f"Selected books: {[book_titles[i-1] for i in selected_indices]}")
print(f"Excluded book (not reading/writing): {excluded_book}")

def analyze_book(content):
    words = content.split()
    word_count = len(words)
    num_paragraphs = content.count('\n\n') + 1
    num_sentences = content.count('. ') + content.count('! ') + content.count('? ')
    smallest_word = min(words, key=len)
    longest_word = max(words, key=len)
    vowel_count = {v: content.lower().count(v) for v in 'aeiou'}
    most_common_vowel = max(vowel_count, key=vowel_count.get)
    punctuation_count = sum(1 for char in content if char in '.,!?;:')
    avg_punctuation_usage = punctuation_count / word_count if word_count > 0 else 0

    return {
        'word_count': word_count,
        'num_paragraphs': num_paragraphs,
        'num_sentences': num_sentences,
        'smallest_word': smallest_word,
        'longest_word': longest_word,
        'most_common_vowel': most_common_vowel,
        'avg_punctuation_usage': avg_punctuation_usage
    }

for i in selected_indices:
    with open(f"book_{i}.txt", "r", encoding="utf-8") as file:
        content = file.read()
        analysis = analyze_book(content)
        print('-' * 50)
        print(f"\nAnalysis of {book_titles[i-1]}:")
        print(f"Word count: {analysis['word_count']}")
        print(f"Number of paragraphs: {analysis['num_paragraphs']}")
        print(f"Number of sentences: {analysis['num_sentences']}")
        print(f"Smallest word: {analysis['smallest_word']}")
        print(f"Longest word: {analysis['longest_word']}")
        print(f"Most common vowel: {analysis['most_common_vowel']}")
        print(f"Average punctuation usage: {analysis['avg_punctuation_usage']:.2f}")
        print('-' * 50)

print(f"Excluded book: {excluded_book}")

endtime = time.time()
print(f"Execution time: {endtime - starttime:.2f} seconds")