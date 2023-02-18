# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Shu Sian (Jessie) Lyu, An Tran
# Date: 2/17/23
# ----------------------------------------------------------------------
"""
Displays statistics about two song lyrics

Module takes two text files from user input.
Then the files are parsed and the following statistics calulated for
both songs:
Total words, distinct words, 8 most common words, longest word,
4-letters+ long words that appear more than 3 times, and common words
between the two lyrics that are 4-letters+ long.
Each statistic is formatted and printed

"""
import string


def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.

    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    word_list = sorted(word_count, key=word_count.get, reverse=True)
    print('The 8 most common words are:')
    for word in range(8):
        print(f'  {word_list[word]}: appears {word_count.get(word_list[word])}'
              f' times.')
    return None


def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    repeat_dict = {word: word_count[word] for word in word_count if
                   len(word) >= 4 and word_count[word] > 3}
    repeat_list = sorted(repeat_dict)
    print('The following (4-letter or longer) words appear more than 3 times:')
    for word in repeat_list:
        print(f'  {word}')
    return None


def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    lyrics = []
    with open(filename, "r") as f:
        text = f.read()
        lyrics = [word.strip(string.punctuation).lower() for word in
                  text.split()]
    return lyrics


def get_stats(words):
    """
    Print the statistics corresponding to the list of words specified.
    :param words: (list of strings) list of lowercase words
    :return: None
    """
    # Call the tally function to build the word count dictionary
    # Then call the appropriate functions and print:
    # 1. The eight most common words in the song in descending order of
    #    frequency, with the number of times they appear.
    # 2. The total number of words in the song.
    # 3. The number of distinct words in the song.
    # 4. The words that are 4-letter or longer and that appear more
    #    than 3 times sorted alphabetically.
    # 5. The longest word.
    word_dict = tally(words)
    print(f'There are {len(words)} words in total in the song.')
    print(f'There are {len(word_dict)} distinct words in the song.')
    most_common(word_dict)
    word_list = sorted(word_dict, key=lambda word: len(word), reverse=True)
    print(f'The longest word in the song is: {word_list[0]}.')
    repeats(word_dict)
    print('-------------------------------------------------------------------'
          '-------------')
    return None


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    common_set = set((word for word in words1 if len(word) >= 4)) & set((
                      word for word in words2 if len(word) >= 4))
    common_list = sorted(list(common_set))
    print('The words (4-letter or longer) that appear in both songs:')
    for word in common_list:
        print(word)


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    lyric_list = []
    filenames = []
    for attempts in range(2):
        filename = input(f'Please enter the filename containing song '
                         f'{attempts + 1}: ')
        filenames.append(filename)
        lyric_list.append(get_words(filename))
    for lyrics in range(2):
        print(f'Song Statistics: {filename}')
        get_stats(lyric_list[lyrics])
    common_words(lyric_list[0], lyric_list[1])


if __name__ == '__main__':
    main()
