from collections import namedtuple

class Coordinate(namedtuple('Coordinate', ['row', 'column'])):
    def __repr__(self) -> str:
        return f'({self.row}, {self.column})'
