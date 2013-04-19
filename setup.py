import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allows setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'tasks',
    version = '0.1',
    packages = ['tasks'],
    include_package_data = True,
    license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    description = 'A module that enables to utilize semantictasks.',
    long_description = README,
    url = 'http://denigma.de',
    author = 'Hevok',
    author_email = 'hevok@denigma.de',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Denigma',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Creative Commons Attribution-Noncommercial-Share Alike license',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP : Dynamic Content',
    ]
)