import math,random
random.seed(2026)
checks=0
for a in [.2,.5,.8]:
 for p1,p2 in [(2,1),(3,4),(.5,2)]:
  for m in [2,8,12]:
   x=a*m/p1;y=(1-a)*m/p2;lam=1/m
   assert abs(p1*x+p2*y-m)<1e-10
   assert abs(a/x-lam*p1)<1e-10 and abs((1-a)/y-lam*p2)<1e-10
   u=x**a*y**(1-a)
   for j in range(1001):
    t=j/1000;gx=t*m/p1;gy=(1-t)*m/p2
    assert gx**a*gy**(1-a)<=u+1e-10
   v=lambda q1,q2,w:math.log(w)-a*math.log(q1)-(1-a)*math.log(q2)+a*math.log(a)+(1-a)*math.log(1-a)
   eps=1e-5
   vm=(v(p1,p2,m+eps)-v(p1,p2,m-eps))/(2*eps)
   vp=(v(p1+eps,p2,m)-v(p1-eps,p2,m))/(2*eps)
   assert abs(-vp/vm-x)<1e-6
   checks+=1
def vlog(r,m):
 if r>=4:return m
 if m<=4-r:return 4*math.log1p(m/r)
 return m-4+r+4*math.log(4/r)

log_cases=[(r,m) for r in [.25,.5,1,2,3.9,4,5,8] for m in [.1,1,3,8]]
log_cases += [(r,4-r) for r in [.5,1,2,3.9]]
for r,m in log_cases:
 q=min(m/r,max(4/r-1,0));aa=m-r*q;value=aa+4*math.log1p(q)
 assert abs(vlog(r,m)-value)<1e-10
 for j in range(1001):
  qq=m/r*j/1000
  assert m-r*qq+4*math.log1p(qq)<=value+1e-10
 lam=1 if r>=4 or m>=4-r else 4/(r+m)
 mua=lam-1;muq=max(r-4,0)
 assert abs(1-lam+mua)<1e-10
 assert abs(4/(1+q)-lam*r+muq)<1e-10
 assert mua>=-1e-10 and muq>=0
 assert abs(mua*aa)<1e-10 and abs(muq*q)<1e-10
 eps=1e-6
 vm=(vlog(r,m+eps)-vlog(r,m-eps))/(2*eps)
 vr=(vlog(r+eps,m)-vlog(r-eps,m))/(2*eps)
 assert abs(-vr/vm-q)<1e-5
 checks+=1

# Roy recovers corners and fixed-proportion demands from value derivatives.
for a,b,p1,p2,m in [(2,1,3,1,12),(2,1,1,1,12),(1,3,2,3,5)]:
 value=lambda pp1,pp2,mm:mm*max(a/pp1,b/pp2)
 eps=1e-6
 vm=(value(p1,p2,m+eps)-value(p1,p2,m-eps))/(2*eps)
 v1=(value(p1+eps,p2,m)-value(p1-eps,p2,m))/(2*eps)
 v2=(value(p1,p2+eps,m)-value(p1,p2-eps,m))/(2*eps)
 expected=(m/p1,0) if a/p1>b/p2 else (0,m/p2)
 assert abs(-v1/vm-expected[0])<1e-6 and abs(-v2/vm-expected[1])<1e-6
 checks+=1
for p1,p2,m in [(2,1,12),(.5,3,8),(4,4,.5)]:
 value=lambda pp1,pp2,mm:mm/(pp1+pp2)
 eps=1e-6
 vm=(value(p1,p2,m+eps)-value(p1,p2,m-eps))/(2*eps)
 for i in [0,1]:
  up=[p1,p2];down=[p1,p2];up[i]+=eps;down[i]-=eps
  vp=(value(*up,m)-value(*down,m))/(2*eps)
  assert abs(-vp/vm-m/(p1+p2))<1e-6
 checks+=1
for _ in range(100):
 p=[random.uniform(.5,5),random.uniform(.5,5)];q=[random.uniform(.5,5),random.uniform(.5,5)]
 m=random.uniform(1,20);n=random.uniform(1,20);t=random.random();a=.4
 v=lambda pp,mm:math.log(mm)-a*math.log(pp[0])-(1-a)*math.log(pp[1])
 mix=[t*p[i]+(1-t)*q[i] for i in range(2)]
 assert v(mix,t*m+(1-t)*n)<=max(v(p,m),v(q,n))+1e-12
 e=lambda pp:8*math.sqrt(pp[0]*pp[1])
 assert e(mix)+1e-12>=t*e(p)+(1-t)*e(q)
 checks+=1
h1=2*math.sqrt(2);h2=4*math.sqrt(2)
assert abs(math.sqrt(h1*h2)-4)<1e-12
assert abs(2*h1+h2-8*math.sqrt(2))<1e-12
assert abs(2-3*1+1)<1e-12
print('Passed:',checks,'parameter scenarios, budget-grid comparisons, KKT residuals, Roy finite differences and compensated-budget checks.')
