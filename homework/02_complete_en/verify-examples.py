#!/usr/bin/env python3
"""Independent grids, numerical envelopes and welfare/risk checks; stdlib only."""
import math
import random
import re
from pathlib import Path

rng=random.Random(20261112)
cases=0


def close(a,b,tol=3e-5):
    assert abs(a-b)<=tol*(1+abs(a)+abs(b)),(a,b)


def partial(f,args,i):
    up,down=list(args),list(args)
    step=1e-5*max(abs(args[i]),.1)
    up[i]+=step;down[i]-=step
    return (f(*up)-f(*down))/(2*step)


def simpson(f,a,b,n=1000):
    step=(b-a)/n
    return step/3*(f(a)+f(b)+sum((4 if k%2 else 2)*f(a+k*step)
                                for k in range(1,n)))


def P(p1,p2):return p1**.25*p2**.75
def ev(p1,p2,u):return u*P(p1,p2)
def vv(p1,p2,m):return m/P(p1,p2)
def xv(p1,p2,m):return (m/(4*p1),3*m/(4*p2))
def hv(p1,p2,u):return (u*P(p1,p2)/(4*p1),3*u*P(p1,p2)/(4*p2))
def primitive(a,b):return 4/(3**.75)*a**.25*b**.75

for _ in range(30):
    p1,p2,m=[rng.uniform(.4,4) for _ in range(3)]
    u=vv(p1,p2,m);x=xv(p1,p2,m)
    close(primitive(*x),u);close(p1*x[0]+p2*x[1],m)
    close(ev(p1,p2,u),m)
    for i in range(2):
        close(hv(p1,p2,u)[i],x[i])
        close(partial(ev,[p1,p2,u],i),x[i])
        close(-partial(vv,[p1,p2,m],i)/partial(vv,[p1,p2,m],2),x[i])
    q1=p1*rng.uniform(1.1,5)
    unew=vv(q1,p2,m)
    cv=ev(q1,p2,u)-m;ee=m-ev(p1,p2,unew)
    cs=simpson(lambda price:xv(price,p2,m)[0],p1,q1)
    close(cs,m/4*math.log(q1/p1))
    assert 0<ee<=cs+1e-7<=cv+1e-7
    old_cost=q1*x[0]+p2*x[1]
    assert ev(q1,p2,u)<=old_cost+1e-8
    assert vv(q1,p2,old_cost)>=u-1e-8
    cases+=1

close(vv(1,1,16),16);close(vv(16,1,16),8)
close(ev(16,1,16)-16,16);close(16-ev(1,1,8),8)
close(simpson(lambda price:4/price,1,16),16*math.log(2))
close(vv(16,1,76),38)
cases+=1


def R(p1,p2):return math.sqrt(p1)+math.sqrt(p2)
def vm(p1,p2,m):return m/R(p1,p2)**2
def em(p1,p2,u):return u*R(p1,p2)**2
def xm(p1,p2,m):return (m/(math.sqrt(p1)*R(p1,p2)),m/(math.sqrt(p2)*R(p1,p2)))
def hm(p1,p2,u):return (u*R(p1,p2)/math.sqrt(p1),u*R(p1,p2)/math.sqrt(p2))
def harmonic(a,b):return a*b/(a+b) if a+b>0 else 0

for _ in range(30):
    p1,p2,m=[rng.uniform(.4,4) for _ in range(3)]
    u=vm(p1,p2,m);x=xm(p1,p2,m)
    close(harmonic(*x),u);close(p1*x[0]+p2*x[1],m)
    close(em(p1,p2,u),m)
    for k in range(501):
        a=m*k/(500*p1);b=max((m-p1*a)/p2,0)
        assert harmonic(a,b)<=u+1e-8
    for k in range(-150,151):
        a=u*(1+math.exp(k/40));b=u*a/(a-u)
        assert p1*a+p2*b>=em(p1,p2,u)-1e-8
    for i in range(2):
        close(hm(p1,p2,u)[i],x[i])
        close(partial(em,[p1,p2,u],i),x[i])
        close(-partial(vm,[p1,p2,m],i)/partial(vm,[p1,p2,m],2),x[i])
    q1=p1*rng.uniform(1.1,5);unew=vm(q1,p2,m)
    cv=em(q1,p2,u)-m;ee=m-em(p1,p2,unew)
    cs=simpson(lambda price:xm(price,p2,m)[0],p1,q1)
    close(cs,2*m*math.log(R(q1,p2)/R(p1,p2)))
    assert 0<ee<=cs+1e-7<=cv+1e-7
    cases+=1

close(vm(1,1,8),2);close(vm(4,1,8),8/9)
close(em(4,1,2)-8,10);close(8-em(1,1,8/9),40/9)
close(simpson(lambda price:xm(price,1,8)[0],1,4),16*math.log(1.5))
cases+=1


lotteries={'A':[(.5,36),(.5,100)],'B':[(.5,4),(.5,132)]}
for name,dist in lotteries.items():
    mean=sum(p*w for p,w in dist)
    eu=sum(p*math.sqrt(w) for p,w in dist)
    ce=eu*eu
    close(mean,68)
    close(ce,64 if name=='A' else 34+2*math.sqrt(33))
    close(mean-ce,4 if name=='A' else 34-2*math.sqrt(33))
    assert ce<mean
    cases+=1
close(math.exp(sum(p*math.log(w) for p,w in lotteries['A'])),60)
assert 64>62>60
for t,sign in [(20,-1),(120,1)]:
    FA=sum(p for p,w in lotteries['A'] if w<=t)
    FB=sum(p for p,w in lotteries['B'] if w<=t)
    assert sign*(FA-FB)>0
close(.5*.75+.5*.25,.5)
close(.75*4+.25*132,36);close(.25*4+.75*132,100)
for b in [math.sqrt,math.log,lambda w:w**.25,lambda w:w]:
    assert sum(p*b(w) for p,w in lotteries['A'])>=sum(p*b(w) for p,w in lotteries['B'])-1e-9
cases+=1


def log_eu(I,W,c,L=84,prob=.25):
    return (1-prob)*math.log(W-c*I)+prob*math.log(W-L+(1-c)*I)

for W in [85,90,100,120,126,140,200]:
    I=max(126-W,0)
    optimum=log_eu(I,W,.5)
    assert all(log_eu(84*k/2000,W,.5)<=optimum+1e-10 for k in range(2001))
    derivative=-.75*.5/(W-.5*I)+.25*.5/(W-84+.5*I)
    if I>0:close(derivative,0)
    else:assert derivative<=1e-10
    cases+=1
close(log_eu(84,100,.25),math.log(79))
assert all(log_eu(84*k/2000,100,.25)<=math.log(79)+1e-10 for k in range(2001))
close(100-.5*26,87);close(16+.5*26,29)
cases+=1


def root_eu(I):return .5*math.sqrt(144-2*I/3)+.5*math.sqrt(16+I/3)
opt=root_eu(40)
assert all(root_eu(128*k/2560)<=opt+1e-10 for k in range(2561))
close(opt*opt,66)
close(.5*(144+16),80);close((.5*(12+4))**2,64)
close(math.sqrt(144-80),8)
close(144-2*40/3,352/3);close(16+40/3,88/3)
close(.5*(352/3+88/3),220/3)
cases+=1

# Counterexamples and qualitative risk restrictions.
u=lambda a,b:max(2*a,b)
close(u(1,0),2);close(u(0,2),2)
assert u(.5,1)<2
x=lambda p1,p2,m:((m-p1)/(2*p1),(m+p1)/(2*p2))
close(partial(lambda a,b,c:x(a,b,c)[0],[1,1,3],1),0)
close(partial(lambda a,b,c:x(a,b,c)[1],[1,1,3],0),.5)
S=[[-4,1],[1,-.25]];price=[1,4]
for row in S:close(sum(a*b for a,b in zip(row,price)),0)
assert .5*(math.sqrt(1)+math.sqrt(9))<math.sqrt(4.5)
assert .5*(1+9)>4.5
assert all(.5*math.log(9-I/2)+.5*math.log(1+I/2)<=math.log(5)+1e-10
           for I in [8*k/1000 for k in range(1001)])
b=lambda w:w if w<=3 else 3+math.log(w-2)
close(.5*b(1)+.5*b(3),b(2))
assert .5*b(4)+.5*b(6)<b(5)
for f in [math.sqrt,math.log,b]:
    for W in [10,100]:
        assert .95*f(W-1)+.05*f(W+9)<f(W)
cases+=1

# Point totals and the number of true/false claims are also part of the audit.
root=Path(__file__).resolve().parent
points=lambda s:sum(map(int,re.findall(r'\\textbf\{(\d+) points\.\}',s)))
assert points((root/'training-consumer.tex').read_text())==30
tr=(root/'training-risk.tex').read_text()
assert points(tr[:tr.index('\\section*{Training 3')])==35
assert points(tr[tr.index('\\section*{Training 3'):])==35
assert points((root/'mock-consumer.tex').read_text())==20
assert points((root/'mock-risk.tex').read_text())==20
claims='\n'.join((root/f).read_text() for f in ['mock-tf-consumer.tex','mock-tf-risk.tex'])
assert list(map(int,re.findall(r'\\task\{(\d+)\.',claims)))==list(range(1,11))
assert 10*5+20+20+2*5==100
print(f'Passed {cases} parameter/data cases plus grading audit: duality, envelopes, '
      'CV/EV/CS, feasible grids, lotteries, dominance, insurance and counterexamples.')
