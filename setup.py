"""
this is the setup of this package.
"""

from setuptools import setup

from sphinxcontrib.table import __version__

with open('sphinxcontrib/requirements.txt', 'r', encoding='utf8') as file:
    install_requires = list(map(lambda x: x.strip(), file.readlines()))

setup(
    name='sphinx-table',
    version='.'.join(map(str, __version__)),
    author='kinopico',
    author_email='zqmillet@qq.com',
    url='https://github.com/zqmillet/sphinx-table',
    description='an extension for sphinx to display excel table in sphinx documents',
    packages=['sphinxcontrib.table'],
    install_requires=install_requires,
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
