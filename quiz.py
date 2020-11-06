import number_theory_functions as num
from rsa_functions import RSA

# Question 2:
q2_answer = num.modular_exponent(23539673, 3434462, 1000) // 100
print(f"Question 2: \nThe hundreds digit of 23539673^3434462 is: {q2_answer}\n")

# Question 3:
print("Question 3:")
p = 3491 
q = 3499
phiN = (p-1)*(q-1)
N = 12215009
decrypted_message = num.modular_exponent(42, num.modular_inverse(3499, phiN), N)
print(f"After using a magic tool we found that {p}*{q} = 12215009.")
print(f"Therefore, phi(12215009) = ({p}-1)*({q}-1) = {phiN}, and we can find the decrypted message: {decrypted_message}\n")

# Question 4:
p, q = 7919, 6841
N = p*q
phiN = (p-1)*(q-1)
d = RSA.generate_private_key(phiN)
e = num.modular_inverse(d, phiN)
key = RSA((N, e), (N, d))
m = 13
encrypted_m = key.encrypt(m)
decrypted_m = key.decrypt(encrypted_m)
print("Question 4:")
print(f"The message chosen to encrypt: {m}")
print(f"The public key is: {e}")
print(f"The encrypted message is: {encrypted_m}")
print(f"The decrypted encrypted message is: {decrypted_m}")

