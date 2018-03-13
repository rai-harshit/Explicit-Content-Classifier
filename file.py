import requests
import json
def score(a):
    b={}
    d={}
    b['text']=a
    d['comment']=b
    d['languages']=["en"]
    c={}
    c['TOXICITY']={}
    d['requestedAttributes']=c
    data=json.dumps(d)
    url = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=AIzaSyBJm4t6BGxGhByZLb7nrqZzMxUaADx2PCU'
    response = requests.post(url, data=data)
    data=json.loads(response.text)
    prob=data['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']
    return prob

with open('/home/vish_master/abc.txt', 'r') as file :
    filedata =file.read()
f= open('/home/vish_master/abc.txt')
for word in f.read().split():
    prob=score(word)
    if(prob>0.75):
        k=len(word)
        rep=''
        for i in range(k):
            rep=rep+'*'
        filedata = filedata.replace(word,rep)
        
with open('/home/vish_master/abc.txt', 'w') as file:
  file.write(filedata)  
#print(response.json())
