from .coordinate import Coordinate

class Span:
    def __init__(self, coordinate: Coordinate, rows: int = 1, columns: int = 1):
        self.coordinate = coordinate
        self.rows = rows
        self.columns = columns

    def __repr__(self):
        return f'<span {self.coordinate} -- ({self.coordinate.row + self.rows - 1}, {self.coordinate.column + self.columns - 1})>'

    def __contains__(self, coordinate):
        return self.coordinate.row <= coordinate.row <= self.coordinate.row + self.rows - 1 and self.coordinate.column <= coordinate.column <= self.coordinate.column + self.columns - 1
