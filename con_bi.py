import pickle

# File paths
input_filename = 'modified_file_with_typos.txt'  # Your existing text file
output_filename = 'binary_test_typo.pkl'  # The new binary file

# Read the content from the text file and split into sentences
with open(input_filename, 'r', encoding='utf-8') as file:
    content = file.read()
    # Split the text content by commas
    sentences_list = content.split(',')

print(len(sentences_list))
print(sentences_list[0:4])  # Print first 4 sentences to check

# Serialize the content and write to a binary file
with open(output_filename, 'wb') as binary_file:
    pickle.dump(sentences_list, binary_file)

print(f"Content has been serialized and saved to {output_filename}")
