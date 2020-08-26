import click
from lib import reader 
from colorama import Fore, Back, Style

template = """{w} ({pos})\n\n{pronunciation}\n\n{definition}"""

class Definition(dict):
    def __init__(self, word:str, data:dict):
        super().__init__(data)
        self.word = word
        self.pos = reader.get_pos(self)

    def show(self, num_def: int=-1):
        num_def = (f'{num_def}: ' if num_def != -1 else '')
        pos = reader.get_pos(self)
        pron = reader.get_pronunciations(self)
        short_def = reader.get_shortdef(self)
        dictionary = 'merriam_webster' # <- TODO: make this dynamic for different dictionary APIs
        # begin terminal print-out
        click.echo()
        click.echo(Fore.GREEN + f'{num_def}{self.word} ({pos})') # <- word (pos)
        click.echo(Style.RESET_ALL)
        click.echo(Fore.LIGHTBLUE_EX + f'pronunciation: {pron}') # <- pronunciation
        click.echo(Style.RESET_ALL)
        click.echo(Fore.BLUE + 'definition: ' + Style.RESET_ALL +  f'{short_def}') # <- short definition
        click.echo()
        click.echo(Fore.YELLOW + 'source: ' + Style.RESET_ALL + f'{dictionary}')
