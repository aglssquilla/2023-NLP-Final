from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import gzip
import json
import os
import time
import re



def simplify(nqexample, n):    
    jsonArray = nqexample['trg'] 
    arr = jsonArray.split(" ")
    if len(arr)>512:
        print(f"length of {n}'th dataset is {len(arr)}")
    return


if __name__=="__main__":
    inpath='/media/disk1/minha/natural-questions/nq_train.jsonl.gz'
    num_processed = 0
    with gzip.open(inpath, "rb") as fin:
        for l in fin:
            num_processed+=1
            utf8_in = l.decode("utf8", "strict")
            son.dumps(simplify(json.loads(utf8_in), num_processed)) + u"\n"

