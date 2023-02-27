# ----------------------------------------------------------------------
# Name:      chat
# Purpose:   implement a simple chatbot
# Author(s):
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

# Enter your constant assignments below
# special topics for rule 2
special_topics = ("family", "friend", "friends", "mom", "dad", "brother",
                  "sister", "girlfriend", "boyfriend", "children", "son",
                  "daughter", "child", "wife", "husband", "home", "dog",
                  "cat", "pet")
# specific words for rule 3
rule3 = ("do", "can", 'will', 'would')
# specific words for rule 7
rule7 = ('need', 'think', 'have', 'want')
# specific words for rule 9
rule9 = ('tell', 'give', 'say')
# pronoun conversion dictionary
pronoun_dict = {'i': 'you', 'am': 'are', 'my': 'your', 'your': 'my',
                'me': 'you', 'you': 'me'}


# Enter the function definition & docstring for the change_person
# function below


def change_person(*words):
    """
    Change pronouns in words to fit response
    :param words: list of words
    :return: returns a string from words in words parameter with
    pronouns changed
    """
    new_words = [pronoun_dict[word] if word in pronoun_dict else word for
                 word in words]
    return ' '.join(new_words)


# Enter function definitions & docstrings for any other helper functions


def chat_with(name):
    """
    Takes a string of users name and prompts user for input. Based off
    of input, chatbot with use match and case statements to pick a
    suitable response.
    :param name: string
    :return: Boolean
    """
    user_input = input("Talk to me please> ")
    # convert user input into list with all lowercase and punctuation
    # stripped words.
    words = [word.strip(string.punctuation) for word in
             user_input.lower().strip(string.punctuation).split()]
    # create set with common topics for rule 2
    common_topics = set(special_topics) & set(words)
    # last character is question mark
    is_question = user_input[-1] == "?"
    match words:
        # rule 1
        case ['bye']:
            return True
        # rule 2
        case _ if common_topics:
            print(f'Tell me more about your '
                  f'{common_topics.pop()}, {name}.')
        # rule 3
        case [question, 'you', *rest] if question in rule3 and is_question:
            no_answer = f'No {name}, I {question} not ' \
                        f'{change_person(*rest)}.'
            question_tuple = (f'Yes i {question}.', no_answer)
            print(random.choice(question_tuple))
        # rule 4
        case ['why', *rest] if is_question:
            print('Why not?')
        # rule 5
        case ['how', *rest] if is_question:
            question_tuple = (f'{name}, why do you ask?', f'{name}, '
                                                          f'how would an '
                                                          f'answer to that'
                                                          f' help you?')
            print(random.choice(question_tuple))
        # rule 6
        case ['what', *rest] if is_question:
            question_tuple = (f'What do you think {name}?', f'Why is that '
                                                            f'important '
                                                            f'{name}?')
            print(random.choice(question_tuple))
        # rule 7
        case ['i', word, *rest] if word in rule7:
            print(f'Why do you {word} {change_person(*rest)}?')
        # rule 8
        case ['i', *rest] if words[-1] != 'too':
            print(f'I {" ".join(rest)} too.')
        # rule 9
        case [verb, *rest] if verb in rule9:
            print(f'You {verb} {" ".join(rest)}.')
        # rule 10
        case _ if is_question:
            question_tuple = ('I have no clue.', 'Maybe.')
            print(random.choice(question_tuple))
        # rule 11
        case _ if 'because' in words:
            print('Is that real reason?')
        # rule 12
        case _:
            question_tuple = ("That's interesting.", "That's nice!",
                              'Can you elaborate on that?')
            print(random.choice(question_tuple))
    return False


def main():
    # Enter your code following the outline below and take out the
    # pass statement.
    # 1.Prompt the user for their name
    # 2.Call chat_with repeatedly passing the name as argument
    # 3.When chat_with returns True, print the goodbye messages.
    # colors = {'red', 'blue', 'yellow'}
    # while True:
    #     rand = colors.pop()
    #     print(rand)
    name = input("Hello. What is your name please? ")
    done = False
    while not done:
        done = chat_with(name)
    print(f'Bye {name}')
    print(f'Have a great day!')


if __name__ == '__main__':
    main()
