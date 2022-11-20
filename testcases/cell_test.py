from pytest import mark

from sphinxcontrib.table.cell import Cell
from sphinxcontrib.table.coordinate import Coordinate
from sphinxcontrib.table.span import Span

@mark.parametrize(
    'text, width, height, rendered_text', [
        (
            'haha',
            10,
            3,
            '+--------+\n' \
            '| haha   |\n' \
            '+--------+'
        ),
        (
            '苟利',
            10,
            3,
            '+--------+\n' \
            '| 苟利   |\n' \
            '+--------+'
        ),
        (
            '苟利',
            10,
            5,
            '+--------+\n' \
            '| 苟利   |\n' \
            '|        |\n' \
            '|        |\n' \
            '+--------+'
        ),
        (
            '苟利',
            20,
            5,
            '+------------------+\n' \
            '| 苟利             |\n' \
            '|                  |\n' \
            '|                  |\n' \
            '+------------------+'
        )
    ]
)
def test_cell_render(text, width, height, rendered_text):
    cell = Cell(text, Coordinate(0, 0), Span(Coordinate(0, 0), rows=1, columns=1))
    assert cell.render(width=width, height=height) == rendered_text
