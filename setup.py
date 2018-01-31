from setuptools import setup, find_packages

__name__ = 'xmltojson'
__author__ = 'John Shanahan'
__author_email__ = 'shanahan.jrs@gmail.com'
__version__ = '0.1.2'
__license__ = 'Apache'
__url__ = 'https://github.com/shanahanjrs/xmltojson'
__description_long__ = """Xmltojson is a Python module and command line application to quickly convert
xml text or files into json."""
__keywords__ = 'xml to json converter'

setup(
    name=__name__,
    version=__version__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    description=__description_long__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'
    ],
    install_requires=[
        'xmltodict'
    ],
    keywords=__keywords__,
    include_package_data=True,
    packages=find_packages('.'),
    py_modules=['xmltojson'],
    scripts=['xmltojson.py']
)
