import hashlib

_input = "iwrupvqb"
final = "AAAAAAAAAAAA"
i = 0

# not my dumb ass brain waiting forever for an infinite while loop (I sat there for 15 minutes before catching up)
# UPDATE : it took 15 seconds lmao
# while final[:5] != "000000": <-- 6 chars
while final[:6] != "000000":
    final = hashlib.md5((_input + str(i)).encode('ascii')).hexdigest()
    i += 1

print(final)
print(i - 1)
