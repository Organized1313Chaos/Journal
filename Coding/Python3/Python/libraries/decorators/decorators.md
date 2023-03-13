- A decorator class in Python is a class that is designed to modify the behavior of functions or other methods. It allows you to add new functionality to existing methods or functions without modifying their source code directly.
<br>
- A decorator class is a class that is designed to be used as a decorator. To create a decorator class, you define a class that implements the __call__ method. The __call__ method takes a function as input, and returns a new function that has the desired behavior.

- Example:
    ```
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

    ```
    ```
    @Timer
    def my_function():
        # function body here

    ```
    ```
    @Timer
    def add_numbers(a, b):
        return a + b

    ```
