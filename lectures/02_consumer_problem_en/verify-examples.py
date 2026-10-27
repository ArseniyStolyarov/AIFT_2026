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
for m in [.5,2,4,8,12]:
 y=min(m,4);aa=m-y;value=aa+4*math.sqrt(y)
 for j in range(1001):
  yy=m*j/1000;assert m-yy+4*math.sqrt(yy)<=value+1e-10
 lam=1 if m>=4 else 2/math.sqrt(m);mu=lam-1
 assert abs(1-lam+mu)<1e-10 and abs(2/math.sqrt(y)-lam)<1e-10
 assert mu>=0 and abs(mu*aa)<1e-10
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
