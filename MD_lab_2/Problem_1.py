import math

key_1 = input("introduce the key 1: ")
key_2 = input("introduce the key 2:")

a = math.gcd(int(key_1,16), int(key_2,16))
print(a % 1000000)