#!/usr/bin/env python3
"""Collate the library French (1998 text) of one book against an OCR page dump of an earlier printing.
Usage: collate_scan.py <BOOK> <dump.fr.txt> <pages.json> <out.json>
pages.json: [[leaf, printed_page, text], ...] from archive.org hOCR.
Reports word-level differences that are not explainable as OCR noise (heuristic)."""
import re,sys,json,difflib,unicodedata
book,dump,pages,outp=sys.argv[1:5]
def strip(s):
    s=unicodedata.normalize('NFKD',s.lower().replace('œ','oe').replace('æ','ae'))
    return ''.join(c for c in s if not unicodedata.combining(c))
def toks(s):
    s=strip(s); s=re.sub(r'-\s*\n\s*','',s)
    return re.findall(r"[a-z0-9]+",s)
T=[];PG=[]
for leaf,pn,text in json.load(open(pages,encoding='utf-8')):
    for w in toks(text): T.append(w); PG.append(pn or f'leaf{leaf}')
n=len(T)
gram={}
for i in range(n-3): gram.setdefault(tuple(T[i:i+4]),[]).append(i)
def lev(a,b):
    if abs(len(a)-len(b))>3: return 9
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        q=[i]
        for j,y in enumerate(b,1): q.append(min(p[j]+1,q[-1]+1,p[j-1]+(x!=y)))
        p=q
    return p[-1]
def noisy(x,y):
    a=''.join(x);b=''.join(y)
    if not a or not b: return len(a)+len(b)<=2
    return lev(a,b)<=max(2,len(a)//4)
res=[];cur=0;found=0;total=0
for l in open(dump,encoding='utf-8'):
    if '\t' not in l: continue
    r,_,t=l.rstrip('\n').split('\t',2); P=toks(t)
    if len(P)<8: continue
    total+=1
    votes={}
    for i in range(0,len(P)-3):
        for p in gram.get(tuple(P[i:i+4]),()):
            s=p-i; votes[s//20]=votes.get(s//20,0)+1
    if not votes: res.append({'ref':r,'status':'not found','words':len(P),'text':t[:200]}); continue
    b=max(votes,key=lambda k:(votes[k],-abs(k*20-cur)))
    if votes[b]<max(2,len(P)//12): res.append({'ref':r,'status':'not found','words':len(P),'text':t[:200]}); continue
    found+=1
    s=max(0,b*20-15); W=T[s:s+len(P)+45]
    sm=difflib.SequenceMatcher(None,P,W,autojunk=False)
    bl=[x for x in sm.get_matching_blocks() if x.size]
    lo=bl[0].b; hi=bl[-1].b+bl[-1].size; a0=bl[0].a; a1=bl[-1].a+bl[-1].size
    sm=difflib.SequenceMatcher(None,P[a0:a1],W[lo:hi],autojunk=False)
    diffs=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal': continue
        x=P[a0:a1][i1:i2]; y=W[lo:hi][j1:j2]
        if noisy(x,y): continue
        diffs.append({'later':' '.join(x),'earlier':' '.join(y),'ctx':' '.join(P[a0:a1][max(0,i1-5):i2+5])})
    if a0>2 or len(P)-a1>2:
        diffs.append({'later':'[edge] '+' '.join(P[:a0])+' … '+' '.join(P[a1:]),'earlier':'?','ctx':''})
    cur=s+lo+len(P)
    if diffs: res.append({'ref':r,'page':PG[min(n-1,s+lo)],'diffs':diffs})
json.dump(res,open(outp,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(book,'paragraphs',total,'located',found,'with differences',sum(1 for x in res if 'diffs' in x),'not found',sum(1 for x in res if x.get('status')))
