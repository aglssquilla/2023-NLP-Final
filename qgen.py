from pprint import pprint
import nltk
nltk.download('stopwords')
from Questgen import main
from datasets import load_dataset
from tqdm import tqdm
import json

dataset = load_dataset("wikitext", 'wikitext-103-v1')
qg = main.QGen()

src_trg_train = []
src_trg_valid = []

nonzero = 0

for i in tqdm(range(dataset['validation'].__len__())):
    text = dataset['validation'].__getitem__(i)['text']
    sen_len = len(text)
    if sen_len < 500 and sen_len >= 200:
        payload = {
            "input_text": f"{text}"
        }
        output = qg.predict_shortq(payload)
        if any(output):
            QA = output['questions']
            for qa in QA:
                ST = {"src": f"{qa['Question']}", "trg": f"{text}"}
                src_trg_valid.append(ST)


with open("./valid.jsonl" , encoding= "utf-8",mode="w") as file: 
	for i in src_trg_valid: file.write(json.dumps(i) + "\n")


for i in tqdm(range(dataset['train'].__len__())):
    text = dataset['train'].__getitem__(i)['text']
    sen_len = len(text)
    if sen_len < 500 and sen_len >= 200:
        payload = {
            "input_text": f"{text}"
        }
        output = qg.predict_shortq(payload)
        if any(output) and nonzero < 50000:
            nonzero += 1
            QA = output['questions']
            for qa in QA:
                ST = {"src": f"{qa['Question']}", "trg": f"{text}"}
                src_trg_train.append(ST)
        elif nonzero >= 50000:
             break


with open("./train.jsonl" , encoding= "utf-8",mode="w") as file: 
	for i in src_trg_train: file.write(json.dumps(i) + "\n")