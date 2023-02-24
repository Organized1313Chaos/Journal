import traceback
import sys

try:
    raise Exception("foo")
except:
    for frame in traceback.extract_tb(sys.exc_info()[2]):
        fname,lineno,fn,text = frame
        print( f"Error in {fname} on line {lineno}")