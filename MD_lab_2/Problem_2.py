import random

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair():
    p = q = 0

    # Step 1: Select two large prime numbers
    while not is_prime(p):
        p = random.randint(50, 1000)
    while not is_prime(q) or q == p:
        q = random.randint(50, 1000)

    # Step 2: Compute n (the modulus)
    n = p * q

    # Step 3: Compute totient (Euler's totient function)
    totient = (p - 1) * (q - 1)

    # Step 4: Select e (public exponent)
    e = random.randint(2, totient)
    while e > 1:
        if gcd(e, totient) == 1:
            break
        e -= 1

    # Step 5: Compute d (private exponent)
    d = modinv(e, totient)

    return ((n, e), (n, d))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(msg, public_key):
    n, e = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in msg]
    return encrypted_msg

def decrypt(encrypted_msg, private_key):
    n, d = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

if __name__ == "__main__":
    # Step 0: Generate key pair
    public_key, private_key = generate_keypair()

    # Step 1: User input
    message = input("Enter a message: ")

    # Step 2: Encryption
    encrypted_message = encrypt(message, public_key)
    print("Encrypted message:", encrypted_message)

    # Step 3: Decryption
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)
