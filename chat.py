# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------
"""
Implementation of a very simple chatbot

Chatbot asks user for name and then asks user for input.
Based off of certain rules, the chatbot will respond with certain
messages. The chatbot can change pronouns to fit the response and
respond with a variety of random responses from the chatbot's response
bank.
"""
import random
import string

# constant assignments
# special topics for rule 2
TOPICS = ("family", "friend", "friends", "mom", "dad", "brother", "sister",
          "girlfriend", "boyfriend", "children", "son", "daughter", "child",
          "wife", "husband", "home", "dog", "cat", "pet")
# pronouns based on user's input
PRONOUNS = {"i": "you", "am": "are", "my": "your",
            "your": "my", "me": "you", "you": "me"}


def change_person(*args):
    """
    Return a string obtained by changing the pronouns based on parameters
    :param args: (tuple) 0 or more additional parameters
    :return: (string) words with changed pronouns
    """
    # change the pronouns if it is in the mapping dictionary
    # otherwise, remain the word the same
    new_words = [PRONOUNS[word] if word in PRONOUNS else word
                 for word in args]

    return ' '.join(new_words)


def chat_with(name):
    """
    Prompt the user for input once only and check if the user enters bye
    with or without a period. If yes, return True without printing anything.
    Otherwise, the function responds according to rules 2-12 given in the
    assignment's description and returns False.
    :param name: (string) name of the user
    :return: (Boolean) True if user inputs bye(.)
             False otherwise
    """
    # list of question words for rule 3
    rule3 = ["do", "can", "will", "would"]
    # list of words for rule 7
    rule7 = ["need", "think", "have", "want"]
    # list of verbs for rule 9
    verbs = ["tell", "give", "say"]

    request = input("Talk to me please> ")

    # lower all letters from the input and
    # separate string into a list of words
    # remove leading and trailing punctuation from each word
    words = [word.strip(string.punctuation) for word in
             request.lower().split()]

    # check if the request is a question
    is_question = (request[-1] == '?')

    # find intersection of words and special topics
    common_topics = set(words) & set(TOPICS)

    match words:
        # rule 1
        case ['bye']:
            return True
        # rule 2
        case _ if common_topics:
            print(f"Tell me more about your {common_topics.pop()}, {name}.")
        # rule 3
        case [question, 'you', *rest] if question in rule3 and is_question:
            changed_pronouns = change_person(*rest)
            response = [f"No {name}, I {question} not {changed_pronouns}.",
                        f"Yes I {question}."]
            print(random.choice(response))
        # rule 4
        case ['why', *rest] if is_question:
            print("Why not?")
        # rule 5
        case ['how', *rest] if is_question:
            response = [f"{name}, why do you ask?",
                        f"{name}, how would an answer to that help you?"]
            print(random.choice(response))
        # rule 6
        case ['what', *rest] if is_question:
            response = [f"What do you think {name}?",
                        f"Why is that important {name}?"]
            print(random.choice(response))
        # rule 7
        case ['i', word, *rest] if word in rule7:
            changed_pronouns = change_person(*rest)  # change the pronouns
            print(f"Why do you {word} {changed_pronouns}?")
        # rule 8
        case ['i', *rest] if words[-1] != "too":
            print(f"I {' '.join(rest)} too.")
        # rule 9
        case [verb, *rest] if verb in verbs:
            print(f"You {verb} {' '.join(rest)}.")
        # rule 10
        case _ if is_question:
            response = ["I have no clue.", "Maybe."]
            print(random.choice(response))
        # rule 11
        case _ if "because" in words:
            print("Is that the real reason?")
        # rule 12
        case _:
            rule12 = ["That's interesting.", "That's nice!",
                      "Can you elaborate on that?"]
            print(random.choice(rule12))

    return False


def main():
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.

    username = input("Hello. What is your name please? ")

    # check if user enters bye(.)
    done = False
    while not done:
        if chat_with(username):
            done = True
            print(f"Bye {username}.")
            print("Have a great day!")


if __name__ == '__main__':
    main()
