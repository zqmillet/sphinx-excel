from typing import List

from .span import Span
from .cell import Cell
from .coordinate import Coordinate

class Spans(dict):
    def add(self, span: Span):
        self[span.coordinate] = span

    def __getitem__(self, coordinate: Coordinate) -> Span:
        if coordinate in self:
            return super().__getitem__(coordinate)
        return Span(coordinate)

    def find(self, coordinate):
        for span in self.values():
            if coordinate in span:
                return span
        return None

class Table:
    def __init__(self, data: List[List[str]], spans=List[Span], headers: int = 1):
        self.headers = headers

        self.spans = Spans()
        for span in spans:
            self.spans.add(span)

        self.cells = []
        self.columns = 0
        self.rows = 0
        for row, texts in enumerate(data):
            for column, text in enumerate(texts):
                self.cells.append(Cell(text=text, span=self.spans[Coordinate(row, column)]))
                self.columns = max(self.columns, column + 1)
            self.rows = max(self.rows, row + 1)
        breakpoint()

    def render(self):
        column_widths = [0] * self.columns
        row_heights = [0] * self.rows
        for cell in self.cells:
            column_widths[cell.coordinate.column] = max(column_widths[cell.coordinate.column], cell.width)
            row_heights[cell.coordinate.row] = max(row_heights[cell.coordinate.row], cell.height)

        string = ''
        for row in range(self.rows):
            cells = [cell for cell in self.cells if cell.coordinate.row == row]
            rendered_text = [
                cell.render(
                    width=column_widths[column],
                    height=row_heights[row],
                    **self.get_cell_border(cell)
                ).splitlines() for column, cell in enumerate(cells)
            ]

            for line in zip(*rendered_text):
                string += ''.join(line)
                string += '\n'

        return string

    def get_cell_border(self, cell):
        border = {}
        # 靠前, 靠上优先显示.
        if cell.coordinate.column == 0:
            border['west'] = '|'
            border['east'] = '|'
        else:
            border['west'] = ''
            border['east'] = '|'

        if cell.coordinate.row == 0:
            border['north'] = '-'
            border['south'] = '-'
        else:
            border['north'] = ''
            border['south'] = '-'

        # 例外情况
        if cell.coordinate.row == self.headers - 1:
            border['south'] = '='

        span = self.spans.find(cell.coordinate)
        if span:
            print(cell.coordinate, span)
        return border
