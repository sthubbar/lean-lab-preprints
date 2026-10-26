# I-0088 numerics: Bordignon-Starichkova, Ramanujan J. 64 (2024), Sec. 5.4 at u=1500, A=10, eps1=1e-20.
# Reproduces eps(1500) by display (6), the Sec. 5.4 total, the binding condition and the range table.
# Needs numpy + mpmath; the sieve to 1e9 takes about 15 s.
import math, numpy as np
from mpmath import mp, mpf, exp, log, euler, quad
mp.dps = 30
def eps_u(u, X=10**9, seg=10**7):            # display (6); tail sum_{p>=X} 1/p^2 <= 2*1.25506/(X log X)
    r = int(X**0.5) + 1; s = np.ones(r + 1, bool); s[:2] = False
    for i in range(2, int(r**0.5) + 1):
        if s[i]: s[i*i::i] = False
    base, parts, lo = np.nonzero(s)[0], [], int(u)
    while lo < X:
        hi = min(lo + seg, X); b = np.ones(hi - lo, bool)
        for p in base[base * base < hi]: b[max(p*p, -(-lo // p) * p) - lo::p] = False
        q = np.nonzero(b)[0] + lo; parts.append(float(np.sum(1.0 / q[q >= u].astype(float)**2))); lo = hi
    S = mpf(math.fsum(parts)) + 2 * mpf('1.25506') / (X * log(X))
    return exp(mpf('1.131e-7') + (mpf(u) / (u - 2) + mpf('0.501')) * S) - 1
g = exp(euler); cb = quad(lambda b: log(2 - 3*b) / (b * (1 - b)), [mpf(1)/8, mpf(1)/3])
def total(a, e, C1, C2, L):                   # 8 Thm5 - (1/2) 8 l1 - (1/2) Thm7, with the 1/L^2 and 1/y terms
    a = mpf(a); k = 8 * (mpf(1)/6 - a); y = L / 3
    t5 = 2*g*log(3 - 8*a)/(4 - 8*a) - e*C2*3*exp(8*a - 2)/(4 - 8*a)
    l1 = (1 + mpf('5e-5')) * (g/4*((log(6) + log((3 - 8*a)/(3 - 18*a)))/(mpf(1)/2 - a) + 512/(k*L**2))
                              + (log(mpf(8)/3) + 64/L**2)*e*C1)
    t7 = (2*g/(mpf(1)/2 - a) + 3*e*C1) * (1 + 1/y + 2/y**2 + 6/y**3) * (cb + 36/L**2 + (log(mpf(8)/3) + 64/L**2)*27/L**2)
    return 8*t5 - 4*l1 - t7/2
def bisect(f, lo, hi):                         # f(lo) false, f(hi) true
    for _ in range(80): m = (lo + hi)/2; lo, hi = (lo, m) if f(m) else (m, hi)
    return hi
e = eps_u(1500); print('eps(1500) = 1/%.4f  < 1/8349: %s' % (1/e, e < mpf(1)/8349))
E, u, A = mpf(1)/8349, 1500, 10
for a, ll in [('0.00256', '13.375'), ('0.0024', '13.45')]:
    L = exp(mpf(ll)); print('alpha %s llX2 %s: total %.6e, (19) a*L-11*ll = %.3f >= 1500' % (a, ll, total(a, E, 112, 114, L), mpf(a)*L - 11*mpf(ll)))
amin = lambda ll: (u + (A + 1)*ll) / exp(ll)
ll1 = bisect(lambda t: mpf('0.00256')*exp(t) - 11*t >= u, mpf(13), mpf(14))
az = bisect(lambda a: total(a, E, 112, 114, exp(mpf('13.375'))) < 0, mpf('0.0025'), mpf('0.0026'))
llo = bisect(lambda t: total(amin(t), E, 112, 114, exp(t)) > 0, mpf(13), mpf(14))
print('binding: (19)/(21)/(25) second part needs llX2 >= %.6f at alpha=0.00256 (slack %.5f);' % (ll1, 13.375 - ll1))
print('  positivity needs alpha < %.7f at llX2=13.375; joint optimum at u=1500: llX2 = %.5f, alpha = %.7f' % (az, llo, amin(llo)))
for a, ll in [('0.00256', '13.375'), ('0.0024', '13.45')]:
    a = mpf(a); L = exp(mpf(ll)); lL = log(L); print('--- ranges at llX2 =', ll, 'alpha =', a)
    rows = [('(19)(21)(25) part 2: a*logX2-11*llX2 >= u', a*L - 11*lL, u), ('(19)(21)(25) part 1: logX2 >= 11/a', L, 11/a),
      ('(25) part 1b: logX2 >= 48(A+4/3)', L, 544), ('(25) part 3 (log): logX2/48-(34/3)llX2 >= log 0.44', L/48 - mpf(34)/3*lL, log(mpf('0.44'))),
      ('alpha1<1/8, alpha3<1/16, alpha2<1/24', a, mpf(1)/24), ('Lemma 7: log z = logX2/8 > 2753', L/8, 2753),
      ('Thm 5: s = 4-8a in [3,4]', 4 - 8*a, 3), ('Thm 6: k = 8(1/6-a) in [1,2]', 8*(mpf(1)/6 - a), 1),
      ('Remark 1: log H = logX2/2-11 llX2 >= log 1e8', L/2 - 11*lL, 8*log(10)), ('Lemma 11: llX2 >= 10', lL, 10),
      ('Lemmas 12-13: logX2 >= log(4e18)', L, log(4e18)), ('Lemma 14: log y = logX2/3 >= log 2657', L/3, log(2657)),
      ('Thm 6 proof: log y >= log 286', L/3, log(286)), ('u in [400, 1e8]', u, 400)]
    for name, v, t in rows: print('  %-52s %16.6f vs %12.6f  %s' % (name, v, t, 'OK' if (v < t if 'alpha1' in name else v >= t) else 'FAIL'))
lN = exp(mpf('13.375'))                         # error terms at log N = e^13.375, U_N >= 0.3706 > 0.37
print('log of 1e5 log^2N N^(-1/8): %.2f' % (log(1e5) + 2*log(lN) - lN/8))
mb = 2*(1 + mpf('1.333')/(lN/2 - 11*log(lN))) * 2/log(2)
print('mbar ~ %.4f (<= 2*1.08*2/log2 = %.4f <= 8); remainder (33) ratio <= %.3e' % (mb, 4*1.08/math.log(2), 0.053*8*(1 + mpf('1e-20'))**0.5/(mpf('0.37')*log(1 + mpf('1e-20'))*lN**6)))
