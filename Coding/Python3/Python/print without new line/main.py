import time

chars = 'ABCDEFGH'
LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence
LINE_UP = '\033[1A' # <-- ANSI sequence

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

print('done')  
print(end=LINE_CLEAR) # <-- clear the line where cursor is located
print('done after.')

# LINE UP clear
print(LINE_UP, end=LINE_CLEAR)