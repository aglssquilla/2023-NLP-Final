# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import requests
from tqdm.auto import tqdm

urls = [   
    "http://dl.fbaipublicfiles.com/KILT/eli5-train-kilt.jsonl",
    "http://dl.fbaipublicfiles.com/KILT/eli5-dev-kilt.jsonl",
    "http://dl.fbaipublicfiles.com/KILT/eli5-test_without_answers-kilt.jsonl",
 ]


for url in urls:
    base = url.split("/")[-1]
    filename = f"data/{base}"
    r = requests.get(url, stream=True)
    # Total size in bytes.
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    t = tqdm(total=total_size, unit="iB", unit_scale=True, desc=base)
    with open(filename, "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
