import hashlib
import time

h=hashlib.new('sha1')
h.update(b"www.google.com"+str.encode(str(time.time())))
print(h.hexdigest()[4:10])
