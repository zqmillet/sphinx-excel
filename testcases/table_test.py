from textwrap import dedent

from sphinxcontrib.table.table import Table
from sphinxcontrib.table.span import Span
from sphinxcontrib.table.coordinate import Coordinate

def test_table():
    table = Table(
        data=[
            ["Header 1", "Header 2", "Header3", "Header 4"],
            ["row 1", "column 2", "column 3", "column 4 苟利"],
            ["row 2", "Cells span columns. and something else", "", ""],
            ["row 3", ".. hint::\n\n    def add(x, y):\n        return x + y", "- Cells\n- contain\n- blocks", ""],
            ["row 4", "", "", ""]
        ],
        spans=[
            Span(Coordinate(2, 1), rows=1, columns=3),
            Span(Coordinate(3, 1), rows=2, columns=1),
            Span(Coordinate(3, 2), rows=2, columns=2)
        ],
        headers=2
    )

    assert table.render() == dedent(
        '''
        +----------+----------------------------------------+-----------+---------------+
        | Header 1 | Header 2                               | Header3   | Header 4      |
        +----------+----------------------------------------+-----------+---------------+
        | row 1    | column 2                               | column 3  | column 4 苟利 |
        +==========+========================================+===========+===============+
        | row 2    | Cells span columns. and something else                             |
        +----------+----------------------------------------+-----------+---------------+
        | row 3    | .. hint::                              | - Cells                   |
        |          |                                        | - contain                 |
        |          |     def add(x, y):                     | - blocks                  |
        |          |         return x + y                   |                           |
        +----------+                                        +                           +
        | row 4    |                                        |                           |
        +----------+----------------------------------------+-----------+---------------+
        '''
    ).strip()
