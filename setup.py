from distutils.core import setup

setup(
    name = 'regscore-py',
    version = '1.0',
    author = 'Ha Dinh, Simran Sethi, Ruoqi Xu',
    author_email = 'dinhhn.ubc@gmail.com, simran.sethi@alumni.ubc.ca, rq658182@dal.ca',
    packages = ['regscore-py'],
    scripts = ['regscore-py/aic.py', 'regscore-py/bic.py', 'regscore-py/mallows.py', 'regscore-py/table.py'],
    url = 'https://github.com/UBC-MDS/regscore-py',
    license = 'LICENSE',
    description = 'Useful score functions to assist regression model comparison',
    long_description = open('README.md').read(),
    install_requires = ['numpy','pandas']
)
