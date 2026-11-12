import re,sys,json,unicodedata
pages,dump=sys.argv[1],sys.argv[2]; refs=sys.argv[3:]
def strip(s):
    s=unicodedata.normalize('NFKD',s.lower().replace('œ','oe'))
    return ''.join(c for c in s if not unicodedata.combining(c))
R=' '.join(re.sub(r'-\n','',t).replace('\n',' ') for _,_,t in json.load(open(pages,encoding='utf-8')))
spans=[(m.group(),m.start(),m.end()) for m in re.finditer(r"[A-Za-zÀ-ÿ0-9]+",R)]
T=[strip(w) for w,_,_ in spans]
gram={}
for i in range(len(T)-3): gram.setdefault(tuple(T[i:i+4]),[]).append(i)
D={l.split('\t')[0]:l.rstrip('\n').split('\t',2)[2] for l in open(dump,encoding='utf-8') if '\t' in l}
for r in refs:
    P=[strip(w) for w in re.findall(r"[A-Za-zÀ-ÿ0-9]+",D[r])]
    votes={}
    for i in range(len(P)-3):
        for p in gram.get(tuple(P[i:i+4]),()): votes[(p-i)//20]=votes.get((p-i)//20,0)+1
    if not votes: print(r,'NOT LOCATED'); continue
    b=max(votes,key=votes.get); s=max(0,b*20-12); e=min(len(spans)-1,s+len(P)+30)
    print(f'--- {r}\n LATER  : {D[r][:900]}\n EARLIER: {R[spans[s][1]:spans[e][2]][:1000]}\n')
