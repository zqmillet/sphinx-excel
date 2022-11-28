"""
this module provides the directive excel.
"""

from docutils.parsers.rst import directives
from docutils.nodes import raw
from docutils.nodes import General
from docutils.nodes import Element
from docutils.nodes import caption
from docutils.parsers.rst.directives.tables import RSTTable
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from openpyxl import load_workbook

from .table import Table
from .span import Span
from .coordinate import Coordinate

class ExcelNode(General, Element):
    """
    excel directive.
    """

class ExcelContentNode(General, Element):
    """
    content of excel.
    """

class ExcelCaptionNode(caption):
    """
    caption of excel directive.
    """

class ExcelDirective(RSTTable):
    """
    an environment for excel
    """

    option_spec = {
        **RSTTable.option_spec,
        'caption': directives.unchanged,
    }
    breakpoint()

    def run(self):
        """Render this environment"""
        caption = self.options.get('caption')
        location, *_ = self.arguments
        file_path, worksheet_name = location.split(':')

        workbook = load_workbook(file_path)
        worksheet = workbook[worksheet_name]
        data = [[str(cell.value) if cell.value is not None else '' for cell in row] for row in worksheet.rows]
        spans = []
        for cell_range in worksheet.merged_cell_ranges:
            spans.append(
                Span(
                    Coordinate(row=cell_range.min_row - 1, column=cell_range.min_col - 1),
                    rows=cell_range.max_row - cell_range.min_row + 1,
                    columns=cell_range.max_col - cell_range.min_col + 1,
                )
            )
        table = Table(data=data, spans=spans)
        print(table.render())
        self.arguments = [caption] if caption else []
        self.content = StringList(table.render().splitlines())
        return super().run()

def visit_excel_node(self, node):
    """
    enter :class:`ExcelNode` in html builder.
    """
    self.body.append(self.starttag(node, "div", CLASS="excel"))

def depart_excel_node(self, _node):
    """
    leave :class:`ExcelNode` in html builder.
    """
    self.body.append("</div>")

def visit_caption_node(self, node):
    """
    enter :class:`ExcelCaptionNode` in html builder
    """
    if not node.astext():
        return

    self.body.append(self.starttag(node, "div", CLASS="excel-caption"))
    self.add_fignumber(node.parent)

    self.body.append(" ")
    self.body.append(self.starttag(node, "span", CLASS="caption-text"))

def depart_caption_node(self, node):
    """
    leave :class:`ExcelCaptionNode` in html builder
    """
    if not node.astext():
        return

    self.body.append("</span>")
    self.body.append("</div>")

def visit_content_node(self, node):
    """
    enter :class:`ExcelContentNode` in html builder.
    """
    self.body.append(self.starttag(node, "div", CLASS='highlight-rst notranslate highlight'))

def depart_content_node(self, _node):
    """
    leave :class:`ExcelContentNode` in HTML builder.
    """
    self.body.append("</div>")

def initialize_numfig_format(_application, config):
    """
    initialize :confval:`numfig_format`.
    """
    config.numfig_format['excel'] = 'Table %s'

def setup(application: Sphinx):
    """
    setup excel directive.
    """

    application.add_directive('excel', ExcelDirective)
    application.connect(event="config-inited", callback=initialize_numfig_format)

    application.add_enumerable_node(
        node=ExcelNode,
        figtype='excel',
        html=(visit_excel_node, depart_excel_node),
        singlehtml=(visit_excel_node, depart_excel_node),
    )
    application.add_node(
        node=ExcelCaptionNode,
        override=True,
        html=(visit_caption_node, depart_caption_node),
        singlehtml=(visit_caption_node, depart_caption_node),
    )
    application.add_node(
        node=ExcelContentNode,
        html=(visit_content_node, depart_content_node),
        singlehtml=(visit_content_node, depart_content_node),
    )
