import os
import requests
from datetime import date
from bs4 import BeautifulSoup
from termcolor import colored

class Input:
    def __init__(self, day=-1, year=-1, input_path=''):
        self._day = date.today().day if day == -1 else day
        self._year = date.today().year if year == -1 else year
        self._input_path = f'input/{self._day}.in' if input_path == '' else input_path
        self._token_path = f'{os.environ["XDG_CONFIG_HOME"]}/.aoc_token' if os.environ["XDG_CONFIG_HOME"] != '' else f"{os.environ['HOME']}/.config/.aoc_token"
        self._session = open(self._token_path).readline().strip()

        if not os.path.exists(self._input_path):
            response = requests.get(
		f'https://adventofcode.com/{self._year}/day/{self._day}/input',
		cookies={"session":self._session},
		headers={
			'User-Agent':'python requests by mislavzanic3@gmail.com'
		}
	    )
            with open(self._input_path, 'w') as f:
                f.write(response.text.strip())

        self._lines = [x.strip() for x in open(self._input_path).readlines()]
        self._string = open(self._input_path).read()


    def submit(self, ans, part):
        if part > 2: return
        response = requests.post(
            f'https://adventofcode.com/{self._year}/day/{self._day}/answer',
                data={
                    'level': str(part),
                    'answer': str(ans)
		},
		cookies={"session":self._session},
		headers={
                    'User-Agent':'python requests by mislavzanic3@gmail.com'
		}
	)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup is not None and soup.article is not None:
            color = 'red'
            if "That's the right answer!" in soup.article.text:
                color = 'yellow'
                message = termcolor.colored(soup.article.text, color)
                print(message)

    def lines(self): return self._lines

    def string(self): return self._string

    def input_path(self): return self._input_path
