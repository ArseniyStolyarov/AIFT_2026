#!/usr/bin/env python3
"""Independent feasible grids, finite differences and boundary-set checks.

Standard library only. Numerical checks supplement the analytical solutions.
"""
import math
import random

rng = random.Random(20261112)
cases = 0


def close(a, b, tol=3e-5):
    assert abs(a-b) <= tol*(1+abs(a)+abs(b)), (a,b)


def partial(f, args, i, relative_step=1e-5):
    up, down = list(args), list(args)
    step = relative_step*max(abs(args[i]),.1)
    up[i] += step
    down[i] -= step
    return (f(*up)-f(*down))/(2*step)


def same_sets(a, b):
    assert len(a)==len(b), (a,b)
    for point in a:
        assert any(all(abs(x-y)<1e-6*(1+abs(x)+abs(y))
                       for x,y in zip(point,other)) for other in b), (a,b)


def u1(a,b): return math.sqrt(a)+2*math.sqrt(b)
def A(p1,p2): return 1/p1+4/p2
def v1(p1,p2,m): return math.sqrt(m*A(p1,p2))
def e1(p1,p2,u): return u*u/A(p1,p2)
def x1(p1,p2,m): return (m/(p1*p1*A(p1,p2)),4*m/(p2*p2*A(p1,p2)))
def h1(p1,p2,u): return (u*u/(p1*p1*A(p1,p2)**2),4*u*u/(p2*p2*A(p1,p2)**2))


for _ in range(30):
    p1,p2 = rng.uniform(.4,3),rng.uniform(.4,3)
    m = rng.uniform(.3,10)
    x = x1(p1,p2,m)
    u = v1(p1,p2,m)
    close(p1*x[0]+p2*x[1],m)
    close(u1(*x),u)
    assert all(t>0 for t in x)
    # Entire exhausted budget, independent of first-order conditions.
    for k in range(1001):
        a=m*k/(1000*p1); b=max((m-p1*a)/p2,0)
        assert u1(a,b)<=u+1e-8
    # Entire target contour in square-root coordinates.
    for k in range(1001):
        z1=u*k/1000; z2=(u-z1)/2
        assert p1*z1*z1+p2*z2*z2>=e1(p1,p2,u)-1e-8
    hh=h1(p1,p2,u)
    same_sets([x],[hh])
    close(e1(p1,p2,u),m)
    close(v1(p1,p2,e1(p1,p2,u)),u)
    vm=partial(v1,[p1,p2,m],2)
    J=[[partial(lambda a,b,c:h1(a,b,c)[i],[p1,p2,u],j)
        for j in range(2)] for i in range(2)]
    for i in range(2):
        close(-partial(v1,[p1,p2,m],i)/vm,x[i])
        close(partial(e1,[p1,p2,u],i),hh[i])
        close(sum(J[i][j]*[p1,p2][j] for j in range(2)),0)
        for j in range(2):
            raw=partial(lambda a,b,c:x1(a,b,c)[i],[p1,p2,m],j)
            income=partial(lambda a,b,c:x1(a,b,c)[i],[p1,p2,m],2)
            close(raw,J[i][j]-x[j]*income)
    close(J[0][1],J[1][0])
    z=[rng.uniform(-3,3),rng.uniform(-3,3)]
    quadratic=sum(z[i]*J[i][j]*z[j] for i in range(2) for j in range(2))
    assert quadratic<=1e-6
    D=p2+4*p1
    close(quadratic,-8*u*u/D**3*(p2*z[0]-p1*z[1])**2)
    M=[[-p2*p2,p1*p2],[p1*p2,-p1*p1]]
    for i in range(2):
        for j in range(2):
            close(J[i][j],8*m/(p1*p2*D*D)*M[i][j])
    same_sets([h1(5*p1,5*p2,u)],[hh])
    close(e1(5*p1,5*p2,u),5*m)
    cases+=1

same_sets([x1(1,4,8)],[(4,1)])
close(v1(1,4,8),4)
close(partial(lambda a,b,c:x1(a,b,c)[0],[1,4,8],0),-6)
close(partial(lambda a,b,c:x1(a,b,c)[0],[1,4,8],2),.5)
close(partial(lambda a,b,c:h1(a,b,c)[0],[1,4,4],0),-4)
cases+=1


def u2(a,b): return max(a+1,math.sqrt(b))
def v2(p1,p2,m): return max(1+m/p1,math.sqrt(m/p2))
def e2(p1,p2,u): return 0 if u<=1 else min(p1*(u-1),p2*u*u)


def X2(p1,p2,m):
    L,R=1+m/p1,math.sqrt(m/p2)
    if abs(L-R)<=1e-10*(1+L+R):return [(m/p1,0),(0,m/p2)]
    return [(m/p1,0)] if L>R else [(0,m/p2)]


def H2(p1,p2,u):
    if u<=1:return [(0,0)]
    C1,C2=p1*(u-1),p2*u*u
    if abs(C1-C2)<=1e-10*(1+C1+C2):return [(u-1,0),(0,u*u)]
    return [(u-1,0)] if C1<C2 else [(0,u*u)]


for ratio in [1,3,4,4.5,6,10]:
 for repeat in range(2):
    p2=rng.uniform(.4,2);p1=ratio*p2
    if ratio>4:
        lo=(ratio-math.sqrt(ratio*ratio-4*ratio))/2
        hi=(ratio+math.sqrt(ratio*ratio-4*ratio))/2
        ml,mh=p2*lo*lo,p2*hi*hi
        incomes=[.5*ml,ml,(ml+mh)/2,mh,2*mh]
        targets=[1+(lo-1)/2,lo,(lo+hi)/2,hi,hi+1]
    else:
        incomes=[p2*k for k in [.5,2,4,8,20]]
        targets=[1.1,1.5,2,3,5]
    for m in incomes:
        u=v2(p1,p2,m);choices=X2(p1,p2,m)
        for a,b in choices:
            close(p1*a+p2*b,m);close(u2(a,b),u)
        for k in range(1001):
            a=m*k/(1000*p1);b=max((m-p1*a)/p2,0)
            assert u2(a,b)<=u+1e-8
        close(e2(p1,p2,u),m)
        same_sets(H2(p1,p2,u),choices)
        if len(choices)==1:
            vm=partial(v2,[p1,p2,m],2)
            roy=tuple(-partial(v2,[p1,p2,m],i)/vm for i in range(2))
            same_sets([roy],choices)
        cases+=1
    for u in targets:
        cost=e2(p1,p2,u);choices=H2(p1,p2,u)
        for a,b in choices:
            close(p1*a+p2*b,cost);close(u2(a,b),u)
        # Sample both branches of the union independently.
        for k in range(501):
            extra=(u-1)*k/500
            assert p1*(u-1)+p2*(u*k/500)**2>=cost-1e-8
            assert p1*extra+p2*u*u>=cost-1e-8
        close(v2(p1,p2,cost),u)
        same_sets(X2(p1,p2,cost),choices)
        same_sets(H2(5*p1,5*p2,u),choices)
        close(e2(5*p1,5*p2,u),5*cost)
        if len(choices)==1:
            gradient=tuple(partial(e2,[p1,p2,u],i) for i in range(2))
            same_sets([gradient],choices)
        cases+=1
    # Both crossings when r>4; the income-only tangency when r=4.
    if ratio>4:
        for m,left_expected,right_expected in [
            (ml,1/p1,1/(2*math.sqrt(ml*p2))),
            (mh,1/(2*math.sqrt(mh*p2)),1/p1)]:
            step=1e-6*m
            left=(v2(p1,p2,m)-v2(p1,p2,m-step))/step
            right=(v2(p1,p2,m+step)-v2(p1,p2,m))/step
            close(left,left_expected);close(right,right_expected)
        cases+=1
    if ratio==4:
        m=4*p2;step=1e-6*m
        close((v2(p1,p2,m)-v2(p1,p2,m-step))/step,1/p1)
        close((v2(p1,p2,m+step)-v2(p1,p2,m))/step,1/p1)
        step=1e-6*p1
        close((v2(p1,p2,m)-v2(p1-step,p2,m))/step,-1/(4*p2))
        close((v2(p1+step,p2,m)-v2(p1,p2,m))/step,0)
        same_sets(X2(p1,p2,m),[(1,0),(0,4)])
        cases+=1
    for u in [-1,0,.5,1]:
        close(e2(p1,p2,u),0)
        same_sets(H2(p1,p2,u),[(0,0)])
        assert u2(0,0)>=u
        cases+=1

# Exact core boundaries and the optional tangency.
same_sets(X2(4.5,1,2.25),[(.5,0),(0,2.25)])
same_sets(H2(4.5,1,1.5),[(.5,0),(0,2.25)])
same_sets(X2(4.5,1,9),[(2,0),(0,9)])
same_sets(H2(4.5,1,3),[(2,0),(0,9)])
assert u2(.25,9/8)<1.5 and u2(1,4.5)<3
same_sets(X2(4,1,4),[(1,0),(0,4)])
same_sets(H2(4,1,2),[(1,0),(0,4)])
close(u2(.5,2),1.5)
for m in [.1,1,4,10]:close(v2(4,1,m),1+m/4)
cases+=1

# Warm-up: a rising Marshallian demand is compatible with utility maximisation
# and a zero compensated derivative. Independently search the whole budget.
def giffen_utility(a,b): return min(a+b,2*a+1.5*b-6)
def giffen_x(p,m): return ((12-m)/(2-p),(2*m-12*p)/(2-p))

for _ in range(30):
    price=rng.uniform(1.02,1.31)
    income=rng.uniform(6*price+.05,11.9)
    xx=giffen_x(price,income)
    target=giffen_utility(*xx)
    assert all(t>0 for t in xx)
    close(price*xx[0]+xx[1],income)
    for k in range(1001):
        a=income*k/(1000*price)
        b=max(income-price*a,0)
        assert giffen_utility(a,b)<=target+1e-8
    dxdp=partial(lambda p,m:giffen_x(p,m)[0],[price,income],0)
    dxdm=partial(lambda p,m:giffen_x(p,m)[0],[price,income],1)
    assert dxdp>0 and dxdm<0
    close(dxdp+xx[0]*dxdm,0)
    same_sets([xx],[(12-target,2*target-12)])
    # Both target constraints imply a piecewise-linear lower frontier.
    # Search that whole frontier beyond either binding intercept as well.
    for k in range(1501):
        a=(target+6)*k/1500
        b=max(target-a,(target+6-2*a)/1.5,0)
        assert price*a+b>=income-1e-8
    cases+=1

print(f'Passed {cases} parameter/data cases: feasible grids, Roy, Shephard, '
      'duality, Slutsky matrix curvature, two switches, tangency, baseline targets '
      'and rising Marshallian demand with zero compensated derivative.')
