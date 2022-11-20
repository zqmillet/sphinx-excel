from .coordinate import Coordinate

class Span:
    def __init__(self, coordinate: Coordinate, rows: int, columns: int):
        self.coordinate = coordinate
        self.rows = rows
        self.columns = columns
