from pytest import mark
from sphinxcontrib.table.text import Text

@mark.parametrize(
    'string, length', [
        ('1234', 4),
        ('苟利', 4),
        ('haha 苟利国家', 13),
    ]
)
def test_text(string, length):
    assert len(Text(string)) == length
