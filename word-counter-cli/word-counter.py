"""
    
    Developer: Kerem Can Belli
    Project: Python Starter Algorithms and CLI Applications
    Subproject: Word Counter
    Description: Updated English version with structured comments
    Last Review: November 2025

"""

##########################################################################

import string

word_counts = {

}

##########################################################################

print("\n--- WORD COUNTER ---")

"""
    
    Project's main menu:

    * This section prepares the file and confirms that the user has entered content into "word-counter.txt".
    * Input is validated using try-except blocks to handle non-integer input.

"""

file = open("python-starter-algorithms/word-counter/word-counter.txt" , "w" , encoding = "utf-8") # "word-counter.txt" file is opened with write mode.
while True:
    try:
        choice_input = input("Please enter any content into 'word-counter.txt'. İf you enter and save please press 1: ")
        choice = int(choice_input) # The input is changed to integer.
        if choice != 1:
            print("Please do not press anything except 1.")
            continue
        break
    except ValueError:
        print("Please input an integer.")
file.close() # "word-counter.txt" file is closed.

##########################################################################

"""

    Word counter section:

    * in this section, the file is opened with read mode.
    * All characters are converted to lowercase.
    * The text is separated (tokenized) into individual words.
    * Punctuation is removed from the cleaned word.

"""

with open("python-starter-algorithms/word-counter/word-counter.txt" , "r" , encoding = "utf-8") as file1: # "word-counter.txt" file is opened with read mode.
    word_list = []
    for line in file1:
        line_words = line.lower().split()    # All characters are converted to lowercase.
                                                    # The text is separated (tokenized) into individual words.
        
        for word in line_words:
            clean_word = word.strip(string.punctuation) # Punctuation is removed from the cleaned word.
            if clean_word:
                word_list.append(clean_word)

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# "word-counter.txt" file is closed.

##########################################################################

"""

    Output section:

    * in this section, all words are sorted by using "sorted" method.
    * the output is demonstrated by using print.

"""

word_pairs = word_counts.items()
sorted_word_twins = sorted(word_pairs , key = lambda item : item[1], reverse=True) # all words are sorted by using "sorted" method.


print("\n--- THE 10 MOST REPEATED WORDS ---")

for word, frequency in sorted_word_twins[:10]:  
    print(f"'{word}': {frequency} times") # the output is demonstrated by using print.