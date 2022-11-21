from unicodedata import east_asian_width
from unicodedata import normalize

from .span import Span

width_map = {
    'F': 1,     # full width
    'H': 1,     # half width
    'W': 2,     # wide
    'Na': 1,    # narrow
    'A': 1,     # ambiguous
    'N': 1,     # neutral
}

def _get_char_display_width(char):
    return width_map.get(east_asian_width(char), 1)

def _get_string_display_width(string):
    return sum(_get_char_display_width(char) for char in string)

class Cell:
    def __init__(self, text: str, span: Span):
        self.text = text
        self.span = span

    def render(self, width, height, top_char: str = '-', bottom_char: str = '-'):
        string = '+' + top_char * (width - 2) + '+\n'
        for index, line in enumerate(self.text.splitlines()):
            string += '| ' + line + ' ' * (width - _get_string_display_width(line) - 4) + ' |\n'

        for _ in range(index, height - 3):
            string += '|' + ' ' * (width - 2) + '|\n'

        return string + '+' + bottom_char * (width - 2) + '+'

    def __repr__(self):
        return f'<cell {self.span} {repr(self.text)}>'

    @property
    def coordinate(self):
        return self.span.coordinate
