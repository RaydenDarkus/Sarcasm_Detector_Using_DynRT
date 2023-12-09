import spacy
from spacy.matcher import Matcher

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def active_to_passive(text):
    # Process the text with spaCy
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)

    # Define a pattern for active sentences
    pattern = [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}]
    matcher.add("ActivePattern", [pattern])

    # Find matches in the text
    matches = matcher(doc)

    # This is where you would add the logic to transform the sentence.
    # This is highly non-trivial and requires handling many cases.
    for match_id, start, end in matches:
        # Extract the matched span
        span = doc[start:end]
        subject = span[0]
        verb = span[1]
        obj = span[2]
        
        # Apply transformation logic
        # This is a simplification and would not work for all sentences
        passive = f"{obj.text} was {verb.lemma_} by {subject.text}"

        # Replace the active voice span with the passive one
        # You need to handle the rest of the sentence and capitalization
        text = text.replace(span.text, passive)

    return text

# Read the text file
with open('test_text_synonyms.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Convert each sentence to passive voice if possible
passive_text = active_to_passive(text)

# Write the converted text to a new file
with open('passive_yourfile_1.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(passive_text)
