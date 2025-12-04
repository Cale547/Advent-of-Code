import requests
import os
from dotenv import load_dotenv  # pip install dotenv
from bs4 import BeautifulSoup  # pip install bs4
import json

MAIN_INPUT_FILENAME = 'input.txt'
TEST_INPUT_FILENAME = 'ex.txt'
USE_SIMPLE_FOLDERNAME = True  #  Simple: "dayN"
ADD_TO_VSCODE_LAUNCH_FILE = False

def get_program_name_a(day: int) -> str:
    return f"lucka{day}a.py" 

def get_program_name_b(day: int) -> str:
    return f"lucka{day}b.py" 


def generate_url(day: int, year: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}"


def fetch_day_soup(day: int, year: int, cache: dict[tuple[int, int]: BeautifulSoup] = {}, force_refetch: bool = False) -> BeautifulSoup:
    if (uid := (day, year)) in cache and not force_refetch:
        return cache[uid]
    url = generate_url(day, year)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    cache[uid] = soup
    return soup


def fetch_day_title(day: int, year: int) -> str:
    soup = fetch_day_soup(day, year)
    h2 = soup.select_one("body > main > article > h2")
    if not h2:
        raise RuntimeError("Could not find puzzle title element.")
    title: str = h2.text
    return f"{str(day)}. {title.removeprefix(f'--- Day {day}: ').removesuffix(' ---')}"


def fetch_day_test(day: int, year: int) -> str:
    soup = fetch_day_soup(day, year)
    code = soup.select_one("body > main > article > pre > code")
    if not code:
        raise RuntimeError("Could not find puzzle test input")
    return code.text

def fetch_day_input(day: int, year: int, session_cookie: str) -> str:
    url = f"{generate_url(day, year)}/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200: return response.text
    else: raise RuntimeError(f"Failed to fetch input: HTTP {response.status_code}")
        

def get_template_code():
    with open("template.py", 'r') as f:
        return f.read()


def add_to_launch_json(day: int, year: int, directory: str):
    filepath = '.vscode/launch.json'
    if not os.path.isfile(filepath):
        struct = {
            'version': '0.2.0',
            'configurations': []
        }
        with open(filepath, 'w') as f:
            f.write(json.dumps(struct, indent=4))
    else:
        with open(filepath, 'r') as f:
            struct = json.loads(f.read())
    struct['configurations'].append({
        'name': f'Python: Y{year} D{day:02}',
        'type': 'debugpy',
        'request': 'launch',
        'program': f'${{workspaceFolder}}/{directory}/{get_program_name_a(day)}',
        'cwd': f'${{workspaceFolder}}/{directory}',
        'console': 'integratedTerminal',
        'justMyCode': True
    })

    struct['configurations'].append({
        'name': f'Python: Y{year} D{day:02}',
        'type': 'debugpy',
        'request': 'launch',
        'program': f'${{workspaceFolder}}/{directory}/{get_program_name_b(day)}',
        'cwd': f'${{workspaceFolder}}/{directory}',
        'console': 'integratedTerminal',
        'justMyCode': True
    })
    with open(filepath, 'w') as f:
        f.write(json.dumps(struct, indent=4))


def main():
    load_dotenv()
    try:
        session_cookie = os.getenv('SESSION_COOKIE')
        have_cookie = session_cookie is not None
    except Exception as e:
        print(f"Error: Could not load session cookie, won't fetch personal input: {e}")
        have_cookie = False
    
    year = int(input("Year: "))
    day = int(input("Day: "))
    while True:
        overwrite = input("Do you want to overwrite files that potentially already exist? (this could overwrite your code) [n/y]: ")
        if overwrite not in ('y', 'n'): 
            print("Only n, or y, is a valid answer")
            continue
        break
    overwrite = True if overwrite == 'y' else False

    if not USE_SIMPLE_FOLDERNAME:
        print("Fetching day title...")
        try:
            day_title = fetch_day_title(day, year)
            print(f"Found day title: {day_title}")
        except:
            print("Error: could not fetch day title")
            day_title = f'day{day}'
    else: 
        day_title = f"{day:02}"

    directory = f'{year}/{day_title}'
    os.makedirs(directory, exist_ok=True)

    if (not os.path.isfile(filepath := os.path.join(directory, MAIN_INPUT_FILENAME)) or overwrite) and have_cookie:
        print(f"Fetching input for {year} Day {day}...")
        try:
            day_input = fetch_day_input(day, year, session_cookie)
            print("Found input!")
        except:
            print(f"Error: could not fetch input for some reason")
            day_input = ''
        with open(filepath, 'w') as f:
            f.write(day_input)
    else:
        print("Input file already exists")

    if not os.path.isfile(filepath := os.path.join(directory, TEST_INPUT_FILENAME)) or overwrite:
        print(f"Fetching test input for {year} Day {day}")
        try:
            test_input = fetch_day_test(day, year)
            print("Found test input!")
        except:
            print(f"Error: could not fetch test input for some reason")
            test_input = ''
        with open(filepath, 'w') as f:
            f.write(test_input)
    else:
        print("Test input file already exists")

    if not os.path.isfile(filepath := os.path.join(directory, get_program_name_a(day))) or overwrite:
        with open(filepath, 'w') as f:
            try:
                template_code = get_template_code()
                f.write(template_code)
            except:
                print("Error: could not find template file")
    else:
        print("Main python file already exists")
    
    if not os.path.isfile(filepath := os.path.join(directory, get_program_name_b(day))) or overwrite:
        with open(filepath, 'w') as f:
            try:
                template_code = get_template_code()
                f.write(template_code)
            except:
                print("Error: could not find template file")
    else:
        print("Main python file already exists")



    if ADD_TO_VSCODE_LAUNCH_FILE:
        print("Adding to VSCode launch.json...")
        try:
            add_to_launch_json(day, year, directory)
            print("Added to launch.json!")
        except Exception as e:
            print(f"Error: could not add to launch.json: {e}")

    print(f"Done, you can access the instructions for this day at {generate_url(day, year)}")


if __name__ == '__main__':
    main()