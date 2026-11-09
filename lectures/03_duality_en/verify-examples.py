#!/usr/bin/env python3
"""Independent numerical checks of the lecture's optimisation examples.

Uses only Python's standard library. These checks complement the analytical
proofs; they do not establish the general theorems.
"""
import math
import random

rng = random.Random(20261109)
cases = 0


def close(a, b, tol=2e-5):
    assert abs(a-b) <= tol*(1+abs(a)+abs(b)), (a, b)


def derivative(f, x, step=1e-5):
    return (f(x+step)-f(x-step))/(2*step)


def budget_maximum(u, p, m, optimum):
    # Independent exhaustive search on the exhausted two-good budget.
    best = max(u(m*j/(2500*p[0]), m*(1-j/2500)/p[1])
               for j in range(2501))
    assert u(*optimum) >= best-1e-8
    close(p[0]*optimum[0]+p[1]*optimum[1], m)


for _ in range(24):
    p1, p2, m = [rng.uniform(.5, 5) for _ in range(3)]
    u = m/(2*math.sqrt(p1*p2))
    e = lambda a, b: 2*u*math.sqrt(a*b)
    h = (u*math.sqrt(p2/p1), u*math.sqrt(p1/p2))
    close(e(p1, p2), m)
    close(h[0], m/(2*p1))
    close(h[1], m/(2*p2))
    close(derivative(lambda a: e(a, p2), p1), h[0])
    close(derivative(lambda b: e(p1, b), p2), h[1])
    budget_maximum(lambda a, b: math.sqrt(a*b), (p1, p2), m, h)
    # Independent expenditure grid, parameterised by the target contour.
    cost = p1*h[0]+p2*h[1]
    assert all(p1*(h[0]*math.exp(j/100))+p2*u*u/(h[0]*math.exp(j/100))
               >= cost-1e-9 for j in range(-300, 301))
    # Concavity, homogeneity, Hessian, Slutsky and all matrix directions.
    q1, q2 = rng.uniform(.5, 5), rng.uniform(.5, 5)
    t = rng.random()
    assert e(t*p1+(1-t)*q1, t*p2+(1-t)*q2) >= t*e(p1,p2)+(1-t)*e(q1,q2)-1e-9
    close(e(3*p1, 3*p2), 3*m)
    S = [[-m/(4*p1*p1), m/(4*p1*p2)],
         [m/(4*p1*p2), -m/(4*p2*p2)]]
    for i in range(2):
        close(sum(S[i][j]*[p1,p2][j] for j in range(2)), 0)
        for j in range(2):
            raw = -m/(2*[p1,p2][i]**2) if i == j else 0
            close(raw, S[i][j]-h[j]/(2*[p1,p2][i]))
    z = [rng.uniform(-3,3), rng.uniform(-3,3)]
    quadratic = sum(z[i]*S[i][j]*z[j] for i in range(2) for j in range(2))
    close(quadratic, -m/4*(z[0]/p1-z[1]/p2)**2)
    assert quadratic <= 1e-9
    cases += 1

for _ in range(12):
    p1, p2, m = [rng.uniform(.5, 5) for _ in range(3)]
    u = m/(p1+p2)
    budget_maximum(min, (p1,p2), m, (u,u))
    close((p1+p2)*u, m)
    close(-m/(p1+p2)**2, -u/(p1+p2))
    # Linear substitutes: the minimum unit price buys the utility target.
    target = rng.uniform(.5, 5)
    costs = [p1*target*j/100+p2*target*(1-j/100) for j in range(101)]
    close(min(costs), target*min(p1,p2))
    cases += 1

def quasi_x(r, m):
    q = min(m/r, max(4/r-1, 0))
    return m-r*q, q


def quasi_h(r, u):
    q = min(math.expm1(u/4), max(4/r-1, 0))
    return max(u-4*math.log1p(q),0), q


for r in [.5, 1, 2, 3, 5, 6]:
    for m in [.3, 1, 3, 10]:
        # Smooth regimes only; the lecture explicitly excludes demand kinks.
        if abs(m-(4-r)) < 1e-6:
            continue
        a, q = quasi_x(r,m)
        u = a+4*math.log1p(q)
        budget_maximum(lambda a,q: a+4*math.log1p(q), (1,r), m, (a,q))
        ha, hq = quasi_h(r,u)
        close(ha,a); close(hq,q)
        e = lambda rr: sum(t*s for t,s in zip((1,rr), quasi_h(rr,u)))
        close(derivative(e,r), q)
        xr = derivative(lambda rr: quasi_x(rr,m)[1],r)
        xm = derivative(lambda mm: quasi_x(r,mm)[1],m)
        hr = derivative(lambda rr: quasi_h(rr,u)[1],r)
        close(xr,hr-q*xm)
        cases += 1

for _ in range(24):
    p2 = rng.uniform(.6,2)
    p1 = p2*rng.uniform(1.05,1.45)
    m = rng.uniform(5*p1+.1*(10*p2-5*p1), 10*p2-.1*(10*p2-5*p1))
    D = 2*p2-p1
    x = ((10*p2-m)/D, (2*m-10*p1)/D)
    utility = lambda a,b: min(a+b,3*a+2*b-10)
    budget_maximum(utility, (p1,p2), m, x)
    u = utility(*x)
    h = (10-u,2*u-10)
    close(h[0],x[0]); close(h[1],x[1])
    # Independent target-feasible cost search, not just the budget problem.
    e = p1*h[0]+p2*h[1]
    assert all(p1*a+p2*max(0,u-a,(u+10-3*a)/2) >= e-1e-8
               for a in [(u+10)*j/2500 for j in range(2501)])
    xp = (10*p2-m)/D**2
    xm = -1/D
    close(xp, -x[0]*xm)
    assert xp > 0 and xm < 0
    eta = (p1-p2)/D
    lam = 1/D
    assert 0 < eta < 1
    close(1+2*eta,lam*p1)
    close(1+eta,lam*p2)
    cases += 1

for _ in range(24):
    p1, p2, p3 = [rng.uniform(.5,3) for _ in range(3)]
    c = p1+p2
    u = math.log(p3/c)+rng.uniform(.3,2)
    q = p3/c
    h3 = u-math.log(q)
    e = p3*(1+u-math.log(p3)+math.log(c))
    close(c*q+p3*h3,e)
    assert h3 > 0
    # Exhaust the target with equal quantities of the complementary composite.
    assert all(c*(q*math.exp(j/100))+p3*max(u-math.log(q*math.exp(j/100)),0)
               >= e-1e-8 for j in range(-300,301))
    close(derivative(lambda b: p3/(p1+b),p2),-p3/c**2)
    assert -p3/c**2 < 0
    cases += 1

# The demand system rejected in slides 51-52.
def rejected(p1,p2,m):
    return [m*p1/(p1*p1+p2*p2), m*p2/(p1*p1+p2*p2)]
raw = [[derivative(lambda p: rejected(p,1,2)[i],1),
        derivative(lambda p: rejected(1,p,2)[i],1)] for i in range(2)]
S = [[raw[i][j]+.5 for j in range(2)] for i in range(2)]
for i in range(2):
    for j in range(2):
        close(S[i][j], .5 if i==j else -.5)
assert S[0][0] > 0
cases += 1

# Finite data: strict two-budget reversal, then a three-cycle without a pair reversal.
p = [(2,1),(1,2)]
x = [(2,1),(1,2)]
dot = lambda a,b: sum(t*s for t,s in zip(a,b))
assert dot(p[0],x[1])==4<5 and dot(p[1],x[0])==4<5
prices = [(2,1,3),(3,2,1),(1,3,2)]
bundles = [(1,0,0),(0,1,0),(0,0,1)]
for i in range(3):
    assert dot(prices[i],bundles[i])==2
    assert dot(prices[i],bundles[(i+1)%3])==1
    assert dot(prices[i],bundles[(i-1)%3])==3
cases += 2

# Diagram coordinates and monetary welfare measures.
A, B, C = (4,4), (2*math.sqrt(2),4*math.sqrt(2)), (2,4)
close(math.sqrt(A[0]*A[1]),4)
close(math.sqrt(B[0]*B[1]),4)
close(dot((2,1),B),8*math.sqrt(2))
close(dot((2,1),C),8)
close(8*math.sqrt(2)-8,3.313708498984761)
close(8-4*math.sqrt(2),2.3431457505076194)
cases += 1

print(f'Passed {cases} parameter/data cases: feasible grids, duality, Shephard, '
      'Slutsky, Giffen KKT, matrix restrictions, revealed preference and welfare.')
