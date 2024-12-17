# Function to separate words into odd and even indexed
def separate_odd_even_indexed_words(sentence):
    words = sentence.split()  # Split the sentence into words
    odd_indexed_words = []   # List for words at odd indexes
    even_indexed_words = []  # List for words at even indexes
    
    # Iterate through words and classify by index
    for index, word in enumerate(words):
        if index % 2 == 0:  # Even index
            even_indexed_words.append(word)
        else:  # Odd index
            odd_indexed_words.append(word)
    
    # Print results
    print("Odd-indexed words  :", ' '.join(odd_indexed_words))
    print("Even-indexed words :", ' '.join(even_indexed_words))

# Input sentence from the user
sentence = input("Enter a sentence: ")
separate_odd_even_indexed_words(sentence)
