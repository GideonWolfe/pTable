from sympy import*
import sys,re
from sympy.solvers import*
from collections import*


def balance2():
    return 'test output'

def balance(q):
    P=str.split
    L=list(map(chr,range(97,123)))
    S,O,a,i,u,v=defaultdict(list),L[:],1,1,'+','->'
    w=u.join
    for p in P(q,v):
     for k in P(p,u):
         c=L.pop(0)
         for e,m in re.findall('([A-Z][a-z]*)(\d*)',k):
          m=int(m or 1)
          a*=m
          S[e][:0]=[c,m*i],
     i=-1
    Y=dict((s,Symbol(s))for s in set(O)-set(L))
    Q=[eval(w('%d*%s'%(c[1],c[0])for c in S[s]),{},Y)for s in S]+[Y['a']-a]
    k=solve(Q,*Y)
    if k:
     N=[k[Y[s]]for s in sorted(Y)]
     g=gcd(N[:1]+N[1::2])
     return(v.join(w((lambda c:str(c)*(c!=1))(N.pop(0)/g)+str(t)for t in P(p,u))for p in P(q,v)))
    else:return('Nope!')
