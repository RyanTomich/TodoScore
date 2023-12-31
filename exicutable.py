import runpy

files = ['functions.py','main.py']
for file in files:
    runpy.run_path(file, run_name='__main__')
