import json
import os
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")

if __name__ == "__main__":
    processed=0
    ks=client["kilt"]
    print(client.list_database_names())
    with open('/media/disk1/minha/KILT/data/nq-dev-kilt.jsonl', 'r', encoding='utf-8') as x:
        with open('/media/disk1/minha/datasets/NQ-full/valid.jsonl','w', encoding='utf-8') as fout:
            with open('/media/disk1/minha/datasets/NQ-full/test.jsonl','w', encoding='utf-8') as fout2:
                for jsonnqall in x:
                    jsonArr={}
                    jsonnq=json.loads(jsonnqall)
                    jsonArr["src"]=jsonnq["input"]
                    n=len(jsonnq["output"])
                    jsonArr["trg"]=""
                    for i in range(len(jsonnq["output"])):
                        if jsonnq["output"][i].get("provenance")==None:
                            continue
                        didx=jsonnq["output"][i]["provenance"][0]
                        jsonkilt=ks.knowledgesource.find_one({"_id":didx["wikipedia_id"]})["text"]
                        for j in range(didx["start_paragraph_id"], didx["end_paragraph_id"]+1):
                            if didx.get("start_character")!=None:
                                processed=processed+1
                                if len(jsonkilt[j])<200:
                                    continue
                                elif len(jsonkilt[j])>500 : 
                                    p=int(len(jsonkilt[j])/500)
                                    q=int(len(jsonkilt[j])/(p+1))
                                    for k in range(p+1):
                                        jsonArr["trg"] = jsonkilt[j][q*k:q*(k+1)]
                                        if processed%100==0:
                                            print(f"{processed} steps processed")
                                        if processed%7==0:
                                            fout.write(json.dumps(jsonArr)+'\n')
                                        else:
                                            fout2.write(json.dumps(jsonArr)+"\n")
                                else :
                                    jsonArr["trg"] = jsonkilt[j]
                                    if processed%100==0:
                                        print(f"{processed} steps processed")
                                    if processed%7==0:
                                        fout.write(json.dumps(jsonArr)+'\n')
                                    else:
                                        fout2.write(json.dumps(jsonArr)+"\n")