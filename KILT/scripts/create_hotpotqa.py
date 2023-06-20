import json
import os
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")

if __name__ == "__main__":
    processed=0
    ks=client["kilt"]
    print(client.list_database_names())
    with open('/media/disk1/minha/KILT/data/hotpotqa-train-kilt.jsonl', 'r') as x:
        with open('/media/disk1/minha/datasets/hotpot/train.jsonl','w') as fout:
#            with open('/media/disk1/minha/datasets/hotpot/test.jsonl','w') as fout2:
            for jsonnqall in x:
                jsonArr={}
                jsonnq=json.loads(jsonnqall)
                jsonArr["src"]=jsonnq["input"]
                n=len(jsonnq["output"])
                jsonArr["trg"]=""
                if jsonnq["output"][0].get("provenance")==None:
                    continue
                didx=jsonnq["output"][0]["provenance"]
                for i in range(len(jsonnq["output"][0]["provenance"])):
                    jsonkilt=ks.knowledgesource.find_one({"_id":didx[i]["wikipedia_id"]})["text"]
                    for j in range(didx[i]["start_paragraph_id"], didx[i]["end_paragraph_id"]+1):
                        jsonArr["trg"] = jsonArr["trg"]+" "+jsonkilt[j][didx[i]["start_character"]:didx[i]["end_character"]]
                if len(jsonArr["trg"])<200 or len(jsonArr["trg"])>500:
                    continue                         
                processed=processed+1
                if processed%100==0:
                    print(f"{processed} steps processed")     
                fout.write(json.dumps(jsonArr)+"\n")
                    
                                
                