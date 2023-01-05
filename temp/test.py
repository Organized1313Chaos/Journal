import time

chars = 'ABCDEFGH'
loop = range(1, len(chars) + 1)

# <-- end without carriage return
for idx in loop:
    print(chars[:idx]) # <-- end without carriage return
    time.sleep(.5)

# <-- end with carriage return
print('='*20)
for idx in loop:
    print(chars[:idx], end='\r') # <-- end with carriage return
    time.sleep(.5)