class MyList(list):
    def __str__(self):
        return "My custom list: " + super().__str__()

# Replace the built-in list class with our custom MyList class
list = MyList

# Now, whenever a list is printed, our custom __str__() method will be called
my_list = [1, 2, 3]
print(my_list)
