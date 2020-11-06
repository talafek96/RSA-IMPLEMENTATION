import number_theory_functions as num
from random import randrange

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p = num.generate_prime(digits)
        q = num.generate_prime(digits)
        N = p*q
        phiN = (p-1)*(q-1)
        d = RSA.generate_private_key(phiN)
        e = num.modular_inverse(d, phiN)
        public_key = (N,e)
        private_key = (N,d)
        return RSA(public_key, private_key)

    @staticmethod
    def generate_private_key(phiN):
        e = randrange(phiN//2 + 1, phiN-1)
        g, _, _ = num.extended_gcd(e, phiN)
        while g != 1:
            e = randrange(phiN//2 + 1, phiN-1)
            g, _, _ = num.extended_gcd(e, phiN)
        return e

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return num.modular_exponent(m, self.private_key[1], self.private_key[0])


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        return num.modular_exponent(c, self.public_key[1], self.public_key[0])
