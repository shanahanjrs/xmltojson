from setuptools import setup, find_packages

import utils

setup(
    name=utils.__name__,
    version=utils.__version__,
    url=utils.__url__,
    author=utils.__author__,
    author_email=utils.__author_email__,
    license=utils.__license__,
    description=utils.__description_long__,
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
    keywords=utils.__keywords__,
    include_package_data=True,
    packages=find_packages('.'),
    py_modules=['xmltojson'],
    scripts=['xmltojson.py', 'scripts/xmltojson']
)
