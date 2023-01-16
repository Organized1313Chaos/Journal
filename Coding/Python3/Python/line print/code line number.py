# This function prints the filename 
# and line number where it is executed
from inspect import currentframe, getframeinfo

cf = currentframe()
filename = getframeinfo(cf).filename

print( getframeinfo(cf) )
print("This is line 5, python says line ", cf.f_lineno)
print("The filename is ", filename)