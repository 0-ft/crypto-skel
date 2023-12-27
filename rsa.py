from utils import mod_inverse, is_prime, indent, dedent, print
import math

class RSA:
    def __init__(self, p=None, q=None, k=None, n=None):
        print("initializing RSA")
        indent()
        self.p = p
        self.q = q
        if p:
            assert is_prime(p)
            print("p is prime ✅")

            if q:
                assert is_prime(q)
                print("q is prime ✅")
                if n:
                    assert n == p * q
                    self.n = n
                    print(f"n = pq = {n} correct ✅")
                else:
                    self.n = p * q if p and q else None
                    print(f"n = pq = {self.n}")
                self.phi = (p - 1) * (q - 1)
                print(f"phi = {self.phi}")
        
        dedent()
        

    def keypair(self, e):
        """
        Generate a keypair using RSA algorithm
        """
        print(f"generating keypair with e = {e}")
        indent()
        assert self.phi
        assert e < self.phi
        assert math.gcd(e, self.phi) == 1
        print("e is coprime to phi ✅")

        d = mod_inverse(e, self.phi)
        print(f"d = {d}")
        kp = ((e, self.n), (d, self.n))
        print(f"keypair = {kp} 🏁")
        dedent()

        return kp

    def encrypt(self, m, e):
        c = pow(m, e, self.n)
        print(f"encrypted message {m}, c = {c} 🏁")
        return c

    def encrypt_block(self, mm, e):
        cc = [pow(m, e, self.n) for m in mm]
        print(f"encrypted message {mm}, c = {cc} 🏁")
        return cc

    def decrypt(self, c, d):
        m = pow(c, d, self.n)
        print(f"decrypted ciphertext {c}, m = {m} 🏁")
        return m

    def decrypt_block(self, cc, d):
        m = [pow(c, d, self.n) for c in cc]
        print(f"decrypted ciphertext {cc}, m = {m} 🏁")
        return m

t = RSA(p=307, q=311)
pk, sk = t.keypair(247)

cc = [94755, 87565, 41862, 49231, 34234, 17479, 26771, 87503]
