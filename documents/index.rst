sphinx-excel
============

简介
----

Sphinx 插入表格有几种方式, 这几种方式都不令人满意.

- ``grid-table``, 表达能力很强, 但是绘制起来很麻烦, 需要专门的编辑器插件辅助完成, 修改起来也不方便.
- ``list-table``, 没办法实现单元格合并, 也不支持环境嵌套.
- ``csv-table``, 可以从 CSV 文件渲染表格, 非常方便, 但是也不支持单元格合并以及环境嵌套.

因此我开发了 sphinx-excel, 可以非常方便的将 excel 文件渲染在 Sphinx 页面中, 并且支持单元格合并以及环境嵌套.

安装
----

可以使用 :numref:`install` 中命令安装 sphinx-excel.

.. _install:
.. bash:: python3 -m pip install sphinx-excel
   :do-not-run:
   :caption: 安装 sphinx-excel

使用
----

首先在 ``conf.py`` 文件中添加如下配置.

.. code-block:: python

    extensions = [
        'sphinxcontrib.excel',
    ]

然后就可以使用 ``excel`` 命令来渲染 excel 表格了, 如 :numref:`render_table_code` 的结果如 :numref:`render_table_result` 所示.

.. _render_table_code:
.. code-block:: rest
    :caption: 渲染 excel 文件

    .. excel:: ./tables.xlsx

.. _render_table_result:
.. excel:: ./tables.xlsx

``excel`` 默认会渲染指定 excel 中的第一个 sheet, 并缺会把第一个 sheet 的名称显示在表格的标题, 如果你不想显示标题, 可以使用 ``:no-caption`` 参数, 如 :numref:`render_table_without_caption_code` 所示.

.. _render_table_without_caption_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 不显示标题

    .. excel:: ./tables.xlsx
       :no-caption:

.. excel:: ./tables.xlsx
   :no-caption:

如果想使用其他标题, 可以使用 ``:caption:`` 参数指定标题, 如 :numref:`render_table_with_caption_code` 所示.

.. _render_table_with_caption_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 指定标题

    .. excel:: ./tables.xlsx
       :caption: 优秀员工

.. excel:: ./tables.xlsx
   :caption: 优秀员工

``excel`` 兼容 Sphinx 内置 ``table`` 命令的所有参数, 比如, 可以使用 ``:align:`` 使表格居中显示, 如 :numref:`render_table_align_center_code` 所示.

.. _render_table_align_center_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 居中显示

    .. excel:: ./tables.xlsx
       :align: center

.. excel:: ./tables.xlsx
   :align: center

如果一个 excel 中有多个 sheet, 可以使用 ``:sheet:`` 参数来指定渲染哪个 sheet, 如 :numref:`render_table_with_sheet_code` 所示.

.. _render_table_with_sheet_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 指定 sheet

    .. excel:: ./tables.xlsx
       :align: center
       :sheet: 员工信息

.. excel:: ./tables.xlsx
   :align: center
   :sheet: 员工信息

值得注意的是, ``excel`` 默认会将第一行加粗, 表示改行是表头, 如果表头行数不为 1, 需要使用 ``:headers:`` 参数指定, 如 :numref:`render_table_with_headers_code` 所示.

.. _render_table_with_headers_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 指定表头行数

    .. excel:: ./tables.xlsx
       :align: center
       :sheet: 复杂表头
       :headers: 2

.. excel:: ./tables.xlsx
   :align: center
   :sheet: 复杂表头
   :headers: 2

``excel`` 命令支持合并单元格的渲染, 并且支持环境嵌套, 如 :numref:`render_table_merged_cell_code` 所示, 其渲染结果如 :numref:`render_table_merged_cell_result` 所示.


.. _render_table_merged_cell_code:
.. code-block:: rest
    :caption: 渲染 excel 文件, 合并单元格

    .. excel:: ./tables.xlsx
       :align: center
       :sheet: 合并单元格
       :headers: 0

.. _render_table_merged_cell_result:
.. excel:: ./tables.xlsx
   :align: center
   :sheet: 合并单元格
   :headers: 0

从 :numref:`render_table_merged_cell_result` 中可以看出表格里可以有任何命令, 可以有代码块, 可以有 ``:admonition:``, 可以有列表, 也可以有公式. 甚至, 代码块是可以被引用的, 如 :numref:`code_demo` 所示.

.. rubric:: footnotes

- :download:`点此下载 <tables.xlsx>` 本文当中使用的 excel 文件.

