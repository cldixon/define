import click 
from lib import dictionary, reader
from lib.definition import Definition

@click.command()
@click.argument('word')
def lookup(word):
    result = dictionary.lookup(word)
    if reader.matches_found(result):
        # matched word definitions returned
        d = Definition(word, result[0]) # <-- only using first definition for now
        click.echo(d.show())
    elif reader.returned_similar_words(result):
        # no matches found; returned similar words
        sep = '- '
        similar_words = f' \n{sep}'.join(result)
        click.echo("No matches found for '{w}'.".format(w=word))
        click.echo(f'Did you mean:')
        click.echo(f'{sep}{similar_words}')
        click.echo()
    else:
        # other results
        click.echo('Unable to parse results.')
