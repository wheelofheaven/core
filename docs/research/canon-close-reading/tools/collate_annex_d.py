import re,difflib,json,unicodedata
L=open('web3/dl/unine.txt',encoding='utf-8').read().split('\n')[10343:11345]
# join entries
txt='\n'.join(l for l in L if not re.match(r'^\s*\d{3}\s*$',l))
ents=re.split(r'\n\s*\n',txt)
E=[]
for e in ents:
    e=' '.join(e.split())
    m=re.match(r'^\*?\s*((?:[1-3] ?)?[A-Z][a-zé]{0,3}) (\d+[^:]{0,24}) : (.+)$',e)
    if m: E.append((m.group(1)+' '+m.group(2),m.group(3)))
def tok(s):
    s=unicodedata.normalize('NFKC',s).lower().replace('’',"'").replace('œ','oe')
    s=re.sub(r'\([^)]*\)\s*\.?\s*$','',s)          # trailing reference
    return re.findall(r"[a-zà-ÿ]+",s)
P=[]
for b in ['TBWTT','ETTMTTP']:
    for l in open(f'texts/{b}.fr.txt',encoding='utf-8'):
        if '\t' in l:
            r,_,t=l.rstrip('\n').split('\t',2); P.append((r,t,tok(t)))
out=[];same=0;nomatch=0
idx={}
for i,(r,t,k) in enumerate(P):
    for w in set(k):
        if len(w)>5: idx.setdefault(w,set()).add(i)
for ref,q in E:
    a=tok(q)
    if len(a)<4: continue
    cand={}
    for w in set(a):
        if len(w)>5:
            for i in idx.get(w,()): cand[i]=cand.get(i,0)+1
    best=None
    for i,_ in sorted(cand.items(),key=lambda x:-x[1])[:8]:
        b=P[i][2]
        sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
        blocks=sm.get_matching_blocks()
        m=sum(x.size for x in blocks)
        if best is None or m>best[0]: best=(m,i,sm)
    if not best or best[0]/len(a)<0.6: nomatch+=1; out.append({'ref':ref,'status':'no match','first':q[:160]}); continue
    m,i,sm=best; b=P[i][2]
    lo=min(x.b for x in sm.get_matching_blocks() if x.size); hi=max(x.b+x.size for x in sm.get_matching_blocks() if x.size)
    sm2=difflib.SequenceMatcher(None,a,b[lo:hi],autojunk=False)
    ops=[(t,' '.join(a[i1:i2]),' '.join(b[lo:hi][j1:j2])) for t,i1,i2,j1,j2 in sm2.get_opcodes() if t!='equal']
    if not ops: same+=1
    else: out.append({'ref':ref,'canon':P[i][0],'diff':ops})
print('entries',len(E),'identical words',same,'different',sum(1 for o in out if 'diff' in o),'no match',nomatch)
json.dump(out,open('ed/annexd.json','w'),ensure_ascii=False,indent=1)
for o in out:
    if 'diff' in o: print(o['ref'],o['canon'],' | '.join(f"{t}: [{x}] -> [{y}]" for t,x,y in o['diff'])[:230])
    else: print(o['ref'],'NO MATCH',o['first'][:120])
