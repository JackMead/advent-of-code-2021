import shutil, os

while True:
    day_number = input("Which day are you creating?")
    try:
        int(day_number)
        break
    except:
        continue

def find_and_replace_in_file(filepath, old, new):
    with open(filepath,'r') as f:
        filedata = f.read()
    newdata = filedata.replace(old, new)
    with open(filepath,'w') as f:
        f.write(newdata)

shutil.copytree('./src/template_day', f'./src/day_{day_number}', ignore=shutil.ignore_patterns('*.pyc', '__pycache__', 'input.txt'))

os.makedirs(f'./tests/day_{day_number}')
shutil.copyfile('./tests/template_tests/test_day.py', f'./tests/day_{day_number}/test_day_{day_number}.py')
shutil.copyfile('./tests/template_tests/__init__.py', f'./tests/day_{day_number}/__init__.py')

find_and_replace_in_file(f'./tests/day_{day_number}/test_day_{day_number}.py', 'X', day_number)
find_and_replace_in_file(f'./src/day_{day_number}/main.py', 'X', day_number)

with open('./pyproject.toml', 'a') as pyproject:
    pyproject.write(f'\nday{day_number} = "src.day_{day_number}.main:run"')