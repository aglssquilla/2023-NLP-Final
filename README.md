# 2023-NLP-Final

* * *
## Dataset
We created training data using [wikitext dataset](https://huggingface.co/datasets/wikitext). The dataset used is "wikitext-103-v1" and this data consists of a total of 1,801,350 train sets and 3,760 validation sets.

From the sentences of the dataset, the [Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) FAQ generation function was used to generate sources corresponding to each target.

The code to generate these data is qgen.py. To reproduce data generation, it is possible to execute as follows.

```bash 
pip install nltk datasets tqdm Questgen
python qgen.py
```

The code loads wikitext data, runs for loop as many times as the number of targets specified in train and validation, and creates at least 1 to maximum 5 questions, that is, sources, through Questgen. Afterwards, the generated sources are saved as .josnl files.


* * *
## Diffuseq
Most of our code was created using [Diffuseq](https://github.com/Shark-NLP/DiffuSeq) as a baseline.   
In order to run our code, we need the corresponding environment, and we can install the environment as follows.

```bash
pip install -r requirements.txt
```

Afterwards, if you put the previously created `valid.jsonl` and `train.jsonl` datasets in the `datasets/` folder, the dataset preparation for train is complete.   
For training, it is possible to execute the following script.

```bash
cd scripts
bash train.sh
```
At this time, various hyperparameters and device settings for train can be modified in `.scripts/train.sh` and applied to train.

* * *
