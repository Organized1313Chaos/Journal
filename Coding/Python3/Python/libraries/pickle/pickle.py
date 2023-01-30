# try:
#     import _pickle as pickle
# except ImportError:
#     import pickle

import pickle

# Create a variable
myvar = [{'This': 'is', 'Example': 2}, 'of',
         'serialisation', ['using', 'pickle']]
  
# The dump(var, file) method dumps a variable into pickle file
with open('file.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(myvar, file)


# The load() method loads a pickled file and returns a deserialized variable.
    
# Load the pickle file
with open('file.pkl', 'rb') as file:
	# Call load method to deserialze
	myvar = pickle.load(file)

print(myvar)
