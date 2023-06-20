import json
import os
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")

if __name__ == "__main__":
    processed=0
    ks=client["kilt"]
    print(client.list_database_names())
    with open('/media/disk1/minha/KILT/data/eli5-train-kilt.jsonl', 'r', encoding='utf-8') as x:
        with open('/media/disk1/minha/datasets/eli5_real/train.jsonl','w', encoding='utf-8') as fout:
    #        with open('/media/disk1/minha/datasets/eli5_real/test.jsonl', 'w', encoding='utf-8') as fout2:
            for jsonnqall in x:
                jsonArr={}
                jsonnq=json.loads(jsonnqall)
                jsonArr["src"]=jsonnq["input"]
                n=len(jsonnq["output"])
                for i in range(len(jsonnq["output"])):
                    if jsonnq["output"][i].get("answer")!=None:
                        jsonArr["trg"]=""
                        jsonArr["trg"]=jsonnq["output"][i]["answer"]
                        if len(jsonArr["trg"])<200 or len(jsonArr["trg"])>500:
                            continue
                        processed=processed+1
                        if processed%100==0:
                            print(f"{processed} steps processed")
                        fout.write(json.dumps(jsonArr)+"\n")
                        
                    
                                    
                    