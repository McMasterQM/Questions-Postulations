import os

path = os.getcwd()
fname = 'QuestionsPostulates.py'

os.system('jupyter nbconvert --to script QuestionsPostulates.ipynb')

with open(fname, 'r') as f:
    lines = f.readlines()
with open(os.path.join(path, 'problem', fname), 'w') as f:
    for line in lines:
        if "get_ipython()" in line:
            continue
        elif 'nbconvert --to script' in line:
            break
        else:
            f.write(line)
os.remove(fname)
