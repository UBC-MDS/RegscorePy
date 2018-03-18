from distutils.core import setup

from setuptools import find_packages

setup(
    name = 'RegscorePy',
    version = '1.0',
    author = 'Ha Dinh, Simran Sethi, Ruoqi Xu',
    author_email = 'dinhhn.ubc@gmail.com, simran.sethi@alumni.ubc.ca, rq658182@dal.ca',
    packages = ['RegscorePy'],
    scripts = ['RegscorePy/aic.py', 'RegscorePy/bic.py', 'RegscorePy/mallow.py'],
    url = 'https://github.com/UBC-MDS/regscore-py',
    license = 'LICENSE',
    description = 'Useful score functions to assist regression model comparison',
    long_description = open('README.md').read(),
    install_requires = ['numpy','pandas'],
    include_package_data=True,
    download_url = 'https://github.com/UBC-MDS/RegscorePy/archive/0.1.tar.gz',
    keywords = ['aic','bic','mallows','regression','scores','machine-learning']
)
