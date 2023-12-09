from transformers import MarianMTModel, MarianTokenizer
import torch
from tqdm import tqdm

# Make sure PyTorch is using the GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the tokenizer and model from the Hugging Face library
model_name = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name).to(device)

def translate(text, model, tokenizer):
    # Tokenize the text
    batch = tokenizer.prepare_seq2seq_batch(src_texts=[text], return_tensors="pt").to(device)
    # Perform the translation
    translated = model.generate(**batch)
    # Decode the translated text
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text[0]

# Read the sentences from the file
with open('op_train_text.txt', 'r', encoding='utf-8') as file:
    sentences = eval(file.read())

# Translate the sentences and save the translations to a list
translated_sentences = [translate(sentence, model, tokenizer) for sentence in tqdm(sentences)]

# Write the translations to a new file
with open('train_text_fr.txt', 'w', encoding='utf-8') as file:
    file.write(str(translated_sentences))

print("Translation completed.")
