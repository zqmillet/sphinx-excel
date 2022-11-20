from unicodedata import east_asian_width
from unicodedata import normalize

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

class Text(str):
    def __len__(self):
        return sum(_get_char_display_width(char) for char in normalize('NFC', self))
