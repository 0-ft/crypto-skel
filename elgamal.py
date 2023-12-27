from utils import is_prime, indent, dedent, print

class ElGamal:
    def __init__(self, p, g):
        print("initializing ElGamal")
        indent()
        self.p = p
        self.g = g
        assert is_prime(p)
        print("p is prime ✅")
        assert g < p
        print("g < p ✅")
        assert g > 0
        print("g > 0 ✅")
        dedent()

    def pubkey(self, d):
        print(f"generating ElGamal pubkey with d = {d}")
        indent()
        assert d < self.p
        print(f"d < p ✅")
        assert d > 0
        print(f"d > 0 ✅")
        pkD = pow(self.g, d, self.p)
        print(f"pkD = g^d mod p = {self.g}^{d} mod {self.p} = {pkD} 🏁")
        dedent()
        return pkD

    def encrypt(self, m, h, pkD):
        print(f"encrypting message {h} with pkD = {pkD}")
        indent()
        assert h < self.p
        print(f"h < p ✅")
        assert h > 0
        print(f"h > 0 ✅")

        pkH = pow(self.g, h, self.p)
        print(f"pkH = g^h mod p = {self.g}^{h} mod {self.p} = {pkH}")

        
        ss = pow(pkD, h, self.p)
        print(f"ss = pkD^h mod p = {pkD}^{h} mod {self.p} = {ss}")

        c = m * ss
        print(f"c = m * ss = {m} * {ss} = {c} 🏁")

        dedent()
        return (pkH, c)

    def decrypt(self, c, pkH, d):
        print(f"decrypting ciphertext {c} with pkH = {pkH} and d = {d}")
        indent()
        ss = pow(pkH, d, self.p)
        print(f"ss = pkH^d mod p = {pkH}^{d} mod {self.p} = {ss}")

        inv = pow(ss, -1, self.p)
        print(f"inv = ss^-1 mod p = {ss}^-1 mod {self.p} = {inv}")

        m = c * inv % self.p
        print(f"m = c * inv mod p = {c} * {inv} mod p = {m} 🏁")

        dedent()
        return m

    def recover_ss(self, m, c):
        print(f"recovering shared secret from message {m} and ciphertext {c}")
        indent()
        m_inv = pow(m, -1, self.p)
        print(f"m^-1 mod p = {m}^-1 mod {self.p} = {m_inv}")
        ss = c * m_inv % self.p
        print(f"ss = c * m^-1 mod p = {c} * {m_inv} mod p = {ss} 🏁")
        dedent()
        return ss

t = ElGamal(37, 2)
pkD = t.pubkey(7)
m = t.decrypt(13, 9, 7)

t.recover_ss(m, 8)