from data import DICTIONARY, LETTER_SCORES
from string import ascii_letters


def load_words():
    """Load dictionary into a list and return list"""
    
    try:
        with open(DICTIONARY, 'r') as f:
            word_lst=f.read().split()
            return word_lst
    except:
            print("Cannot open file {d}".format(d=DICTIONARY))


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_score=0
    for letter in word.upper():
        if letter in ascii_letters:
            word_score+=LETTER_SCORES[letter]
    return word_score


def max_word_value(word_lst=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores_lst=[]
    for word in word_lst:
        scores_lst.append(calc_word_value(word))
    max_word_index=scores_lst.index(max(scores_lst))
    return word_lst[max_word_index]
    

if __name__ == "__main__":
    pass # run unittests to validate
