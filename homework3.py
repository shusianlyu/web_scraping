# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Shu Sian (Jessie) Lyu, An Tran
# Date: 02/17/2023
# ----------------------------------------------------------------------
"""
implementation of language statistics based on lyrics of two songs

User inputs two text file names that contains the lyrics of songs
For each song, this program compute and print (ignore capitalization):
1. The total number of words in the song.
2. The number of distinct words in the song.
3. The eight most common words in descending order of frequency.
4. The longest word in the song.
5. The words that are 4-letter or longer that appear more than 3
times sorted alphabetically.
Finally, print the words (4-letter or longer) that appear in
both songs, listed alphabetically.
"""
import string


def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    words_dic = {}  # dictionary with form words
    for i in words:
        # increment count of each word in the song
        words_dic[i] = words_dic.get(i, 0) + 1

    return words_dic


def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.

    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    # sort the words based on their number of times they appear
    # in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1],
                               reverse=True)
    # for loop to iterate 8 times
    for word in sorted_word_count[:8]:
        print(f"  {word[0]}: appears "
              f"{word[1]} times.")


def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    # get a list of 4-letter or longer words that
    # appear more than 3 times alphabetically
    words = sorted({word for word in word_count
                    if word_count[word] > 3 and len(word) >= 4})

    for word in words:
        print(f"  {word}")


def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    with open(filename, "r") as f:
        lyrics = f.read()
        # convert all the words to lowercase and
        # stripped of punctuation
        words = [word.lower().strip(string.punctuation)
                 for word in lyrics.split()]

    return words


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
    word_counts = len(words)  # total number of words
    words_dic = tally(words)  # build the word count dictionary
    distinct_words = len(words_dic)  # number of distinct words
    longest = max(words_dic.keys(), key=len)  # longest word

    print(f"There are {word_counts} words in total in the song.")
    print(f"There are {distinct_words} distinct words in the song.")
    print("The 8 most common words are:")
    most_common(words_dic)  # eight most common words
    print(f"The longest word in the song is: {longest}.")
    print("The following (4-letter or longer) words "
          "appear more than 3 times:")
    repeats(words_dic)  # words that repeat more than 3 times


def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    # compare length of two lists and check if the word
    # in longer list appear in the shorter list
    # use set to store common words as it only contains unique data
    commons = ({word for word in words1 if len(word) >= 4}&
               {word for word in words2 if len(word) >= 4})

    # print the common words
    for i in sorted(commons):
        print(i)


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    filenames = []  # list to store filenames
    words = []  # list to store words in each file

    # loop to prompt user for filenames
    for i in range(2):
        filename = input(f"Please enter the filename containing song "
                         f"{i + 1}: ")
        # append each filename to the list
        filenames.append(filename)
        # append words in each file to the list
        words.append(get_words(filenames[i]))

    # loop to print the statistics corresponding to each song
    for i in range(2):
        print(f"Song Statistics: {filenames[i]}")
        get_stats(words[i])
        print("----------------------------------------"
              "----------------------------------------")

    # report on words common to both songs
    print("The words (4-letter or longer) that appear in both songs:")
    common_words(words[0], words[1])


if __name__ == '__main__':
    main()