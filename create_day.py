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

year = 0
while year not in ["2021", "2023"]:
    year = input("Which year do you want?")

shutil.copytree('./src/template_day', f'./src/year_{year}/day_{day_number}', ignore=shutil.ignore_patterns('*.pyc', '__pycache__', 'input.txt'))

os.makedirs(f'./tests/year_{year}/day_{day_number}')
shutil.copyfile('./tests/template_tests/day.py', f'./tests/year_{year}/day_{day_number}/test_day_{day_number}.py')
shutil.copyfile('./tests/template_tests/__init__.py', f'./tests/year_{year}/day_{day_number}/__init__.py')
shutil.copyfile('./tests/template_tests/test_input.txt', f'./tests/year_{year}/day_{day_number}/test_input.txt')

find_and_replace_in_file(f'./tests/year_{year}/day_{day_number}/test_day_{day_number}.py', 'X', day_number)
find_and_replace_in_file(f'./tests/year_{year}/day_{day_number}/test_day_{day_number}.py', 'Y', year)
find_and_replace_in_file(f'./src/year_{year}/day_{day_number}/main.py', 'X', day_number)
find_and_replace_in_file(f'./src/year_{year}/day_{day_number}/main.py', 'Y', year)

# with open('./pyproject.toml', 'a') as pyproject:
#     pyproject.write(f'\nday{day_number} = "src.year_{year}.day_{day_number}.main:run"')