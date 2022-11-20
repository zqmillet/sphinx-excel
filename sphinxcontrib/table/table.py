from typing import List

from .span import Span

class Table:
    def __init__(self, data: List[List[str]], spans=List[Span]):
        self.data = data
        self.spans = spans
