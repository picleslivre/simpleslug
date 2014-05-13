import unicodedata

__version__ = '1.0.0.dev1'

def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFD', data) if unicodedata.category(x)[0] == 'L' or x == ' ').lower()


def slugfy(string, separator='-'):
    output = remove_accents(string.strip()).replace(' ', separator)

    while separator+separator in output:
        output = output.replace(separator+separator, separator)

    return output
