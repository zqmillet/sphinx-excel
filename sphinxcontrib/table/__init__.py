"""
this is the package sphinxcontrib.console.
"""
__version__ = (1, 0, 9)

from os.path import join
from os.path import dirname

from sphinx.util.fileutil import copy_asset

from .excel import setup as setup_excel

def copy_asset_files(application, execution):
    """
    this function is used to copy css file to build directory.
    """
    asset_files = [join(dirname(__file__), 'sphinx_console.css')]
    if execution is None: # build succeede
        for path in asset_files:
            copy_asset(path, join(application.outdir, '_static'))

def setup(application):
    """
    setup extension.
    """
    setup_excel(application)

    return {"version": __version__, "parallel_read_safe": True}
