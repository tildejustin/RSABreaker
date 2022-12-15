from Cryptodome.PublicKey import RSA
import factorise

key = RSA.importKey(open("smallkey.pem", "rb").read())
print(key.n, key.e)

factors = factorise.factorise(key.n)
print(factors)
