import click 
from lib import dictionary, reader
from lib.definition import Definition
from colorama import Fore, Back, Style

@click.command()
@click.argument('word', default='')
@click.option('--pos', type=str, default=None, help='Filters results by part-of-speech (e.g. noun, verb).')
@click.option('--set_dict', type=str, default=None, help='Set default dictionary for lookups.')
def get_definition(word: str, pos: str, set_dict: str):
    if word == '':
        if set_dict is not None:
            click.echo("... will set/update the default dictionary here.")
            click.echo("... also will ask for ")
    else:
        result = dictionary.lookup(word)
        if reader.matches_found(result):
            # matched word definitions returned
            ## filter results 
            definitions = dictionary.filter(result, pos)
            for i,d in enumerate(definitions):
                d = Definition(word, d)
                d.show(num_def=i+1)
                click.echo()
                click.echo('-' * 35)
        elif reader.returned_similar_words(result):
            # no matches found; returned similar words
            sep = '- '
            similar_words = f' \n{sep}'.join(result)
            click.echo(Fore.RED + "No matches found for '{w}'.".format(w=word))
            click.echo(Style.RESET_ALL)
            click.echo(f'Did you mean:')
            click.echo(f'{sep}{similar_words}')
            click.echo()
        else:
            # other results
            click.echo('Unable to parse results.')