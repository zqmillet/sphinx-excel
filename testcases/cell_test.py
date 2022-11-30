from pytest import mark

from sphinxcontrib.excel.cell import Cell
from sphinxcontrib.excel.coordinate import Coordinate
from sphinxcontrib.excel.span import Span

@mark.parametrize(
    'text, width, height, rendered_text', [
        (
            'haha',
            10,
            3,
            '+--------+\n'
            '| haha   |\n'
            '+--------+'
        ),
        (
            '苟利',
            10,
            3,
            '+--------+\n'
            '| 苟利   |\n'
            '+--------+'
        ),
        (
            '苟利',
            10,
            5,
            '+--------+\n'
            '| 苟利   |\n'
            '|        |\n'
            '|        |\n'
            '+--------+'
        ),
        (
            '苟利',
            20,
            5,
            '+------------------+\n'
            '| 苟利             |\n'
            '|                  |\n'
            '|                  |\n'
            '+------------------+'
        ),
        (
            '',
            10,
            3,
            '+--------+\n'
            '|        |\n'
            '+--------+'
        ),
        (
            '哈，哈',
            10,
            3,
            '+--------+\n'
            '| 哈，哈 |\n'
            '+--------+'
        )

    ]
)
def test_cell_render(text, width, height, rendered_text):
    cell = Cell(text, Span(Coordinate(0, 0), rows=1, columns=1))
    assert cell.render(width=width, height=height) == rendered_text

@mark.parametrize(
    'text, width, height, north, south, west, east, rendered_text', [
        (
            'haha',
            10,
            3,
            '=',
            '-',
            '|',
            '|',
            '+========+\n'
            '| haha   |\n'
            '+--------+'
        ),
        (
            '苟利',
            10,
            3,
            '-',
            '=',
            '|',
            '|',
            '+--------+\n'
            '| 苟利   |\n'
            '+========+'
        ),
        (
            '苟利',
            10,
            3,
            '',
            '=',
            '|',
            '|',
            '| 苟利   |\n'
            '+========+'
        ),
        (
            '苟利',
            10,
            3,
            '-',
            '=',
            '',
            '|',
            '--------+\n'
            ' 苟利   |\n'
            '========+'
        ),
        (
            '苟利',
            10,
            3,
            '-',
            '=',
            '',
            '',
            '--------\n'
            ' 苟利   \n'
            '========'
        ),
        (
            '苟利',
            10,
            4,
            '',
            '=',
            '',
            '',
            ' 苟利   \n'
            '        \n'
            '========'
        )
    ]
)
def test_cell_render_with_border_char(text, width, height, north, south, west, east, rendered_text):
    cell = Cell(text, Span(Coordinate(0, 0), rows=1, columns=1))
    assert cell.render(width=width, height=height, north=north, south=south, west=west, east=east) == rendered_text
