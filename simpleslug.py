import sys
import unicodedata

__version__ = '1.0.0.dev1'
__all__ = ['ensure', 'JsonProbe']

# --------------
# Py2 compat
# --------------
PY2 = sys.version_info[0] == 2

if PY2:
    string_types = (str, unicode)
else:
    string_types = (str,)
# --------------


def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFD', data) if unicodedata.category(x)[0] == 'L' or x == ' ').lower()


def slugfy(string, separator='-'):
    output = remove_accents(string.strip()).replace(' ', separator)

    while separator+separator in output:
        output = output.replace(separator+separator, separator)

    return output
