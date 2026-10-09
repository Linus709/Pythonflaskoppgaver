import bcrypt

passord = "passord1234" .encode('utf=8')
hashed = bcrypt.hashpw(passord, bcrypt.gensalt())

print("orginalt passord:", passord)
print("kryptert passord:", hashed)

passordInput = input("skriv inn passordet: ").encode('utf-8')
if bcrypt.checkpw(passordInput, hashed):
    print("Passordet stemmer!")
else:
    print("Feil passord!")