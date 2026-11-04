"""Independent budget-grid, KKT and finite-difference checks; standard library only."""
import math
import random

checks = 0

def near(a, b, tol=1e-8):
    assert abs(a-b) <= tol * (1+abs(a)+abs(b)), (a, b)

def partial(fun, args, i):
    eps = 1e-6
    up, down = list(args), list(args)
    up[i] += eps
    down[i] -= eps
    return (fun(*up)-fun(*down))/(2*eps)

# Problem 1: fixed-price KKT regimes, checked against a separate feasible grid.
for m in [.1, .5, 1, 2, 5, 12]:
    if m <= 1:
        x1, x2, lam, mu2 = m, 0, 1/(1+m), (1-m)/(1+m)
    else:
        x1, x2, lam, mu2 = (m+1)/2, (m-1)/4, 2/(m+3), 0
    near(x1+2*x2, m)
    near(1/(1+x1)-lam, 0)
    near(1/(1+x2)-2*lam+mu2, 0)
    near(mu2*x2, 0)
    assert mu2 >= -1e-10
    best = math.log1p(x1)+math.log1p(x2)
    for j in range(1001):
        a=m*j/1000; b=(m-a)/2
        assert math.log1p(a)+math.log1p(b) <= best+1e-10
    checks += 1

vg = lambda p1,p2,m: 2*math.log(m+p1+p2)-math.log(4*p1*p2)
for p1,p2,m in [(1,2,5),(2,1,5),(1,1,2),(.5,3,8)]:
    S=m+p1+p2
    expected=[S/(2*p1)-1,S/(2*p2)-1]
    vm=partial(vg,[p1,p2,m],2)
    for i in [0,1]:
        near(-partial(vg,[p1,p2,m],i)/vm, expected[i], 1e-6)
    checks += 1

# Problem 2: all regions and both transition types.
def vq(r,m):
    if r >= 2: return m+4
    if m <= 4/r-r: return 4*math.sqrt(1+m/r)
    return m+r+4/r

cases=[(r,m) for r in [.25,.5,1,1.5,2,3] for m in [.25,1,6,20]]
cases += [(r,4/r-r) for r in [.5,1,1.5]]
for r,m in cases:
    q=min(m/r,max(4/r**2-1,0)); a=m-r*q
    lam=1 if r>=2 or m>=4/r-r else 2/(r*math.sqrt(1+m/r))
    mua=lam-1; muq=max(r-2,0)
    near(1-lam+mua,0)
    near(2/math.sqrt(1+q)-lam*r+muq,0)
    near(mua*a,0); near(muq*q,0)
    assert mua >= -1e-10 and muq >= 0
    best=a+4*math.sqrt(1+q)
    near(vq(r,m),best)
    for j in range(1001):
        qq=m/r*j/1000
        assert m-r*qq+4*math.sqrt(1+qq) <= best+1e-10
    near(-partial(vq,[r,m],0)/partial(vq,[r,m],1),q,1e-5)
    checks += 1

# Problem 3: augmented linear programme and nonunique boundary sets.
def vmin(p1,p2,m):
    return m*max(1/p1,1/p2,3/(p1+p2))

rng=random.Random(2026)
cases=[(p1,1,12) for p1 in [.25,.5,1,2,3]]
cases += [(rng.uniform(.2,4),rng.uniform(.2,4),rng.uniform(.5,20)) for _ in range(25)]
for p1,p2,m in cases:
    S=p1+p2
    if p1 < p2/2:
        x1,x2=m/p1,0; lam=1/p1; e1,e2=0,1; mu1,mu2=0,p2/p1-2
    elif p1 > 2*p2:
        x1,x2=0,m/p2; lam=1/p2; e1,e2=1,0; mu1,mu2=p1/p2-2,0
    else:
        x1=x2=m/S; lam=3/S; e1,e2=(2*p1-p2)/S,(2*p2-p1)/S; mu1=mu2=0
    t=min(2*x1+x2,x1+2*x2)
    near(1-e1-e2,0)
    near(2*e1+e2-lam*p1+mu1,0)
    near(e1+2*e2-lam*p2+mu2,0)
    near(lam*(m-p1*x1-p2*x2),0)
    near(e1*(2*x1+x2-t),0); near(e2*(x1+2*x2-t),0)
    near(mu1*x1,0); near(mu2*x2,0)
    assert min(lam,e1,e2,mu1,mu2) >= -1e-10
    near(vmin(p1,p2,m),t)
    for j in range(1001):
        a=m/p1*j/1000; b=(m-p1*a)/p2
        assert min(2*a+b,a+2*b) <= t+1e-9
    if not math.isclose(p1/p2,.5) and not math.isclose(p1/p2,2):
        vm=partial(vmin,[p1,p2,m],2)
        for i,expected in enumerate([x1,x2]):
            near(-partial(vmin,[p1,p2,m],i)/vm,expected,1e-5)
    checks += 1
for p1,p2 in [(.5,1),(2,1)]:
    m=12; balanced=(m/(p1+p2),)*2
    corner=(m/p1,0) if p1<p2 else (0,m/p2)
    for j in range(11):
        w=j/10; x=[w*corner[i]+(1-w)*balanced[i] for i in [0,1]]
        near(p1*x[0]+p2*x[1],m)
        near(min(2*x[0]+x[1],x[0]+2*x[1]),vmin(p1,p2,m))
    left=(vmin(p1,p2,m)-vmin(p1-1e-6,p2,m))/1e-6
    right=(vmin(p1+1e-6,p2,m)-vmin(p1,p2,m))/1e-6
    assert abs(left-right)>1
    checks += 1
print(f'Passed {checks} parameter cases: independent budget grids, full KKT, Roy derivatives and boundary demand segments.')
