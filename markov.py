"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #open file, store as txt_file
    with open(file_path) as txt_file:
        #.read() creates one line of text
        full_text = txt_file.read()

    #return line of text
    return full_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    #entire one line, txt string
    word = text_string.split()

    #loop through length of word, stop at 2nd from last
    for i in range(len(word) - 2):     
        key = (word[i], word[i+1])
        #if tuple of 2 words not in dict keys
        #instantiate empty list
        #lst_chains holds every 3rd word
        #instantiate k(2 words),v pair          
        if key not in chains.keys():        
            lst_chains = []                 
            lst_chains.append(word[i+2])    
            chains[key] = lst_chains        
        else:
            # update_list = chains[key]       #store value of keys
            # update_list.append(word[i+2])   #update value
            # chains[key] = update_list       #update k,v pair                                   
            chains[key].append(word[i+2])    
        
    return chains


def make_text(chains):
    """Return text from chains."""

    words = [] 
    #randomizes tuple from chains
    new_key = choice(chains.keys())
    print new_key
    words.extend([new_key[0], new_key[1]])
    #until there is no tuple 
    while new_key in chains:
        #random_word pulls from v corresponding to randomly selected k
        random_word = choice(chains[new_key])
        new_key = (new_key[1], random_word)
        words.append(random_word)

    return " ".join(words)


input_path = "rfrost.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
