- `nano new_file_name`
  creates a new file if it doesn't exist else opens a file with given name.
- `ctrl+ o` to rename the file
- `mkdir direcory_name` to create a directory name
- `cat file_name` displays content of the file in file_name
- `cat > test` write in a file named 'test', ctrl+D to exit 
- `cat > file_name` to overwritten the complete file
- `cat >> file_name` to append at the end of the file
- `chmod -w file_name` to change the file permissions, <br>-w simply removes the write permission , +w adds the write permissions
- ```$$ ==> gives PID of the process```
- `cd ~` : Go to home directory

**Signals**
- `Ctrl + C, interrupt signals , signal term: sigInt`
- `Ctrl + Z, suspend signals , signal term: sigTSTP`
- `kill -9 (SIGKILL signal) <PID>`
- `man 7 signal --> List of signals`
- `trap "echo signal is detected" SIGINT`
- `SIGKILL and SIGSTOP cannot be caught using sigkill`
- `trap "rm -f $file: exit" 0 2 15`
  removes a file on the interrupts 0 (successful file execution), 2, 15
- debug code: 
  `Method 1: bash -x ./filename.sh`
  `Method 2:` `#!/bin/bash -x` ( include the line at the top)
  `Method 3:` `set -x` will start debugging at random line_number
  set +x to deactivate the debugging mode
<br>

- **Download and Installation**
  - `sudo apt-get install vlc`

