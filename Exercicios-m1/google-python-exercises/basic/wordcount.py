#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def get_file_words_hank(filename):
    '''
    get_file_works_hank
    
    Obtem as palavras contidas no arquivo e retorna um dicionário 'hankeado'
    com a contagem de palavras contidas no arquivo.
    '''
    
    dic_cont = {}
    
    arquivo = open(filename)
    
    # Remover pontuação e tudo que não interessa para compor palavras.
    arq_buff = re.sub(u'?!{[|}]()=', ' ', arquivo.buffer)
    arq_buff = re.sub(u'\'.,;:,"´', '', arq_buff)
    
    lst = list(str(str(str(arq_buff).lower()).split()))
    arquivo.close()
    
    
    for item in lst:
        dic_cont[item] += 1
    
    return dic_cont

def print_words(filename):
    '''
    Faz a impressão das palavras com a quantidade de incidências dentro do 
    texto.
    '''
    
    palavras_qt = get_file_words_hank(filename)
    print('Counting words: ')
    for item in palavras_qt:
        print(item.key + ' ' + item.value)


def print_top(filename):
    '''
    Faz a impressão das 20 primeiras palavras de maior incidência.
    '''
    
    palavras_qt = get_file_words_hank(filename)
    
    sorted(palavras_qt.items(), key=lambda x: x[1], reverse=True)
    print('Top counting words: ')
    for item in palavras_qt:
        n += 1
        if n > 20: Break
        print(str(n) + ' ' + item.key + item.value)

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
