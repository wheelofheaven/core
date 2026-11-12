import re,sys,json
def toks(s): return re.findall(r"[a-z0-9]+", s.lower().replace('’',"'").replace("'",''))
raw=open('pdf/id.en.txt',encoding='utf-8',errors='replace').read().split('\n')
# drop running heads / page numbers
lines=[l for l in raw if not re.match(r'^\s*\d+\s*$',l) and not re.match(r'^\s*([A-Z] ?){6,}',l.strip()[:40].replace(' ','')) ]
def region(a,b):
    return toks(' '.join(raw[a:b]))
import bisect
out={}
for book,(a,b) in {'TBWTT':(715,5260),'ETTMTTP':(5260,9390)}.items():
    T=region(a,b); n=len(T)
    pos={}
    for i,t in enumerate(T):
        if len(t)>4: pos.setdefault(t,[]).append(i)
    cur=0; res=[]; covered=[False]*n
    for l in open(f'texts/{book}.en.txt',encoding='utf-8'):
        if '\t' not in l: continue
        r,_,t=l.rstrip('\n').split('\t',2)
        P=toks(t); W=set(x for x in P if len(x)>4)
        if len(W)<6: res.append((r,None,len(P))); continue
        L=max(30,int(len(P)*1.4)); best=(0,None)
        lo=0; hi=n
        # candidate starts: positions of paragraph words in range
        cand=set()
        for w in W:
            ps=pos.get(w,[]); i0=bisect.bisect_left(ps,lo); i1=bisect.bisect_right(ps,hi)
            for p in ps[i0:i1]: cand.add(max(0,p-L//2)//10*10)
        for c in cand:
            win=set(T[c:c+L+L//2])
            sc=len(W&win)/len(W)
            if sc>best[0] or (sc==best[0] and best[1] is not None and abs(c-cur)<abs(best[1]-cur)): best=(sc,c)
        if best[0]>=0.5:
            c=best[1]; res.append((r,round(best[0],2),len(P)))
            for k in range(c,min(n,c+L+L//2)): covered[k]=True
            cur=c+len(P)
        else: res.append((r,round(best[0],2),len(P)))
    un=[x for x in res if x[1] is not None and x[1]<0.5]
    print(book,'paras',len(res),'matched',sum(1 for x in res if x[1] and x[1]>=0.5),'unmatched',len(un),'short',sum(1 for x in res if x[1] is None))
    print(' unmatched:',[(x[0],x[1],x[2]) for x in un if x[2]>=25][:70])
    # uncovered stretches in ID
    gaps=[];i=0
    while i<n:
        if not covered[i]:
            j=i
            while j<n and not covered[j]: j+=1
            if j-i>=70: gaps.append((i,j-i,' '.join(T[i:i+14])))
            i=j
        else: i+=1
    print(' ID stretches not matched (>=70 tokens):',len(gaps))
    for g in gaps[:40]: print('   ',g)
