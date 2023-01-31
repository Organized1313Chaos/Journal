# os.system(string_command)
# execute string command, returns exit status  

# ================================================
'''
The following code executes commands in cmd
and directly returns 0 if successful, -1 otherwise
'''
# ================================================
import os 
hello =  os.system('echo Hello')
print(hello)
all_dirs =  os.system('dir')
print(all_dirs)
# ================================================
'''
The following code returns the command line output 
and stores it as a variable
'''
# ================================================
import subprocess
output = subprocess.check_output("dir", shell=True)
print(output)
# ================================================

from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("echo hello world")
# Or
my_output = out(["echo", "hello world"])

# ================================================

#Useful Commands
#File name only, directory not included
current_script_name = os.path.basename(__file__)
print(current_script_name)

#get the path of the base_dir//file_name.py
#you have to import inspect 
from inspect import getsourcefile
base_dir = os.pth.abspath(getsourcefile(lambda:0))

## Get the path of the particular directory only
file_dir_path_only = os.path.dirname(os.path.realpath(__file__))