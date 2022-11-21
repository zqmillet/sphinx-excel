from typing import List

from .span import Span
from .cell import Cell
from .coordinate import Coordinate

class Table:
    def __init__(self, data: List[List[str]], spans=List[Span]):
        self.data = data
        self.spans = {span.coordinate: span for span in spans}
        breakpoint()

    def render(self):
        cells = []
        for row_index, row in enumerate(self.data):
            for column_index, text in enumerate(row):
                coordinate = Coordinate(row_index, column_index)
                cells.append(
                    Cell(
                        text=text,
                        coordinate=coordinate,
                        span=self.spans.get(coordinate, Span(coordinate))
                    )
                )
        breakpoint()
