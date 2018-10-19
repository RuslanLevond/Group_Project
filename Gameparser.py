import string
#List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    #This function filters user's input using skip_words dictionary.
    new_words = words.copy()
    
    for n_word in words:
        for s_word in skip_words:
            if(n_word == s_word):
                new_words.remove(n_word)
    return new_words

    
def remove_punct(text):
    #This removes all of the punctuation
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    #Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    no_punct = no_punct.split()
    no_punct = filter_words(no_punct, skip_words)
    return no_punct
