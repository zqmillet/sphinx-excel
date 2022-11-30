# sphinx-excel <img src = "./documents/statics/logo.png" height = 120 align="right"> 

[![sphinx-excel](https://img.shields.io/badge/pypi-sphinx--excel-brightgreen)](https://pypi.org/project/sphinx-excel/)
[![Documentation Status](https://readthedocs.org/projects/sphinx-excel/badge/?version=latest)](https://sphinx-excel.readthedocs.io/en/latest/?badge=latest)
![pytest](https://github.com/zqmillet/sphinx-excel/actions/workflows/pytest.yml/badge.svg)
![mypy](https://github.com/zqmillet/sphinx-excel/actions/workflows/mypy.yml/badge.svg)
![flake8](https://github.com/zqmillet/sphinx-excel/actions/workflows/flake8.yml/badge.svg)
![pytest](https://github.com/zqmillet/sphinx-excel/actions/workflows/pytest.yml/badge.svg)

## introduction

sphinx-excel uses `openpyxl` to read an excel file and render it into sphinx document.

## installation

you can install sphinx-excel by `pip`.

``` bash
python3 -m pip install sphinx-excel
```

## setup

please add `sphinxcontrib.excel` into your `conf.py` file.

``` python
extensions = [
    'sphinxcontrib.excel',
]
```

## usage

the following code will insert the first sheet of `tables.xlsx` into sphinx document.

``` rst
.. excel:: ./tables.xlsx
```

the `excel` directive will show the sheet name as the caption of table. you can use `:no-caption` to remove it.

``` rst
.. excel:: ./tables.xlsx
   :no-caption:
```

if you want to specify the caption, you can use `:caption:` argument.

``` rst
.. excel:: ./tables.xlsx
   :caption: hello world
```

`excel` directive supports all arguments of sphinx native `table` directive. for example, you can use `:align:` to change table align style.

``` rst
.. excel:: ./tables.xlsx
   :align: center
```

if an excel file contains more than one sheets, you can use `:sheet:` arguments to specify which sheet to be rendered.

``` rst
.. excel:: ./tables.xlsx
   :align: center
   :sheet: stuff
```

the first line of table is in bold font, it means that the first line is header of table. if the table has two rows header, you can use `:headers:` to tell `excel` directive.

``` rst
.. excel:: ./tables.xlsx
   :headers: 2
```

## one more thing

`excel` directive supports to render merged cell in excel. the content of the cell can be:

- math equtions,
- code snippets, and
- other directives.
