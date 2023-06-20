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
## myTokenizer
We provide modified version of 'p_sample' and 'myTokenizer'. The 'myTokenizer class provides tokenization and detokenization functionalities, and it also introduces the ability to add noise tokens to the input sequences.

The 'myTokenizer' class has the following functionalities:
Loading a tokenizer: It can load a tokenizer from either a BERT configuration or a defined BPE vocabulary dictionary. The tokenizer can be loaded using the BERT configuration name or by specifying the path to the vocabulary file.

Encoding tokens: It provides a method called encode_token that takes a list of sentences as input and converts them into tokenized sequences. It supports both dictionary-based tokenization and the PreTrainedTokenizerFast tokenization method from the Hugging Face library.

Decoding tokens: It offers a method called decode_token that takes a sequence of token IDs and decodes them back into human-readable tokens. This method supports both dictionary-based decoding and decoding using the PreTrainedTokenizerFast library.

Adding noise tokens: The Modified_myTokenizer class extends the original encode_token method by adding a randomly generated noise token to each input sequence. The noise token is inserted at a random position between the [START] token and the [END] token. This allows the tokenizer to handle noisy or corrupted input data.

* * *
## p_sample
The 'p_sample' function incorporates x_{t-2} in addition to x_{t-1} when generating the noise for sampling from the model. 

The function first calculates the mean and variance of the model's output at x_{t-1} using the p_mean_variance function. It then generates two noise tensors, noise_t1 and noise_t2, using th.randn_like based on x_t1 and x_t2 respectively. If top_p is specified and greater than 0, the noise tensors are clipped using the top-p sampling method. 

The code ensures that the absolute values of the noise tensors are within the top-p range. A nonzero mask is created based on the value of t to indicate whether noise should be added. If t is 0, no noise is added. The final sample tensor is calculated by adding the mean and variance weighted noise tensors to the model's mean output. 

If a mask is provided, the sample tensor is modified by replacing the masked positions with the corresponding values from x_start.
* * *
