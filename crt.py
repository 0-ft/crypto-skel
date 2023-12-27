from utils import mod_inverse, is_prime, indent, dedent, print
import math

# (divisor, remainder) pairs
def crt_combine(modpairs, N):
    print(f"solving system of congruences mod {N} using CRT")
    indent()
    assert len(modpairs) > 0
    assert all([a == b or math.gcd(a, b) for a, _ in modpairs for b, _ in modpairs])
    print("all pairs are coprime ✅")
    yz = []
    for i, (n, a) in enumerate(modpairs):
        print(f"x = {a} mod {n}")
        indent()
        yi = N // n
        print(f"y = N / {n} = {yi}")
        # zi = mod_inverse(yi, n)
        zi = pow(yi, -1, n)
        print(f"z = y^-1 = {zi}")
        yz.append((yi, zi))
        dedent()
    print(f"solution = sum(y * z * a) = {' + '.join([f'({y} * {z} * {a})' for (y, z), (_, a) in zip(yz, modpairs)])}")
    sol = sum([y * z * a for (y, z), (_, a) in zip(yz, modpairs)])
    for (n, a) in modpairs:
        assert sol % n == a
    print(f"solution = {sol} = {sol % N} mod {N} 🏁")
    dedent()

crt_combine([(7, 3), (5, 2), (3, 2), (2, 1)], 210)

