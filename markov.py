from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open file and read into memory
    text = open(file_path).read().rstrip()

    # Replace newlines with space
    #text = text.replace('\n', ' ')

    return text


def make_chains(text_string, ngrams):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    # split text in to list of words
    words = text_string.split()
    chains = {}

    # get n-grams starting at each word
    for x in range(len(words[:-ngrams])):
        key = tuple(words[x:x + ngrams])

        # add n-grams to dictionary
        if key in chains:
            chains[key].append(words[x + ngrams])
        else:
            chains[key] = [words[x + ngrams]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []

    # Starting ngram (as tuple)
    start = choice(chains.keys())

    # Add starting ngram to text list
    text.extend(start)

    while True:
        # Choose next word randomly from list
        new_word = choice(chains[start])

        # Add new word to text list
        text.append(new_word)

        # Generate tuple for next ngram
        new_key = start[1:] + (new_word,)

        # Break out of loop if bigram doesn't exist
        if new_key in chains:
            start = new_key
        else:
            break

    # Return text list formatted as string
    return ' '.join(text)

input_path = sys.argv[1]
ngrams = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, ngrams)

# Produce random text
random_text = make_text(chains)

print random_text
