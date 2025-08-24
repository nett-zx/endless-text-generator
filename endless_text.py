import hashlib
import string
import time

alphanum = string.ascii_letters
while True:
    h = hashlib.sha256(str(time.time_ns()).encode()).hexdigest()
    print(''.join(alphanum[int(h[i:i+2], 16) % len(alphanum)] for i in range(0, len(h), 2)))