import time

class Timer:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time} seconds to execute.")
        return result

# =================EXAMPLE=============================
@Timer
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
# Output: Function add_numbers took 3.0994415283203125e-06 seconds to execute
print(result)
# Output: 5
