- **Virtual Environment**
`step 1`: `python -m venv venv`
`step 2`: `venv\Scripts\activate`
<br>

- **Requirements**
  `GET`:  `pip freeze >requirements.txt`
  `run`:  `pip install -r requirements.txt`
  <br>

  to install dependencies without error, run the following command.
  
  `windows`: 
  `FOR /F %k in (requirements.txt) DO ( if NOT # == %k ( pip install %k ) )`
  
  `ubuntu`: 
  `cat requirements.txt | xargs -n 1 pip install`
<br>

- **Version Control**
`step 1`: `git init`
`step 2`: Create a `.gitignore` file for trivial files to avoid unneccessary tracking of files
<br>

- **Debug Code**
`step 1`: Create `launch.json` file using vscode debugger sidebar
`step 2`: Make sure of specified configuration path to run project properly 

  
  
  