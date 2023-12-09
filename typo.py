import random
import nltk
nltk.download('punkt')

# Function to introduce a typo into a word
def introduce_typo(word):
    if len(word) < 3:  # Avoid changing very short words
        return word
    typo_type = random.choice(['swap', 'insert', 'delete'])
    index = random.randint(1, len(word)-2)  # Avoid start and end of the word
    if typo_type == 'swap':
        # Swap two adjacent characters
        word = word[:index] + word[index+1] + word[index] + word[index+2:]
    elif typo_type == 'insert':
        # Insert a random character
        random_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        word = word[:index] + random_char + word[index:]
    elif typo_type == 'delete':
        # Delete a character
        word = word[:index] + word[index+1:]
    return word

# Function to randomly introduce typos into sentences from a file
def introduce_typos_to_file(file_path, num_typos):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = nltk.sent_tokenize(text)
    
    for _ in range(num_typos):
        sentence_index = random.randint(0, len(sentences)-1)
        words = sentences[sentence_index].split()
        word_index = random.randint(0, len(words)-1)
        words[word_index] = introduce_typo(words[word_index])
        sentences[sentence_index] = ' '.join(words)
    
    return ' '.join(sentences)

# Path to your file
file_path = 'modified_file.txt'
num_typos = 200  # Number of typos you want to introduce

# Introduce typos into the file
modified_text = introduce_typos_to_file(file_path, num_typos)

# Save the modified text to a new file
with open('modified_file_with_typos.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(modified_text)
