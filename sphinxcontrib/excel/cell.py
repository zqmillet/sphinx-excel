from unicodedata import east_asian_width

from .span import Span
from .coordinate import Coordinate

width_map = {
    'F': 2,     # full width
    'H': 1,     # half width
    'W': 2,     # wide
    'Na': 1,    # narrow
    'A': 1,     # ambiguous
    'N': 1,     # neutral
}

def _get_char_display_width(char: str) -> int:
    return width_map.get(east_asian_width(char), 1)

def _get_string_display_width(string: str) -> int:
    return sum(_get_char_display_width(char) for char in string)

class Cell:
    def __init__(self, text: str, span: Span):
        self.text = text
        self.span = span

    def render(self, width: int, height: int, south: str = '-', north: str = '-', west: str = '|', east: str = '|') -> str:
        south_east = '+' if south and east else ''
        south_west = '+' if south and west else ''
        north_east = '+' if north and east else ''
        north_west = '+' if north and west else ''

        if south == ' ' and east == ' ':
            south_east = ' '
        elif south == ' ' and west == ' ':
            south_west = ' '
        elif north == ' ' and east == ' ':
            north_east = ' '
        elif north == ' ' and west == ' ':
            north_west = ' '

        if north:
            string = north_west + north * (width - 2) + north_east + '\n'
        else:
            string = ''

        index = 0
        for line in self.text.splitlines():
            string += west + ' ' + line + ' ' * (width - _get_string_display_width(line) - 4) + ' ' + east + '\n'
            index += 1

        for _ in range(index, height - 2):
            string += west + ' ' * (width - 2) + east + '\n'

        if south:
            return string + south_west + south * (width - 2) + south_east
        return string

    def __repr__(self) -> str:
        return f'<cell {self.span} {repr(self.text)}>'

    @property
    def coordinate(self) -> Coordinate:
        return self.span.coordinate

    @property
    def width(self) -> int:
        return 4 + max((_get_string_display_width(line) for line in self.text.splitlines()), default=0)

    @property
    def height(self) -> int:
        return 2 + len(self.text.splitlines())
