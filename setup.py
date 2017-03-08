from setuptools import setup, find_packages
import xmltojson

setup(
    name='xmltojson',
    version=xmltojson.__version__,
    url='https://github.com/shanahanjrs/xmltojson',
    author=xmltojson.__author__,
    author_email='shanahan.jrs@gmail.com',
    license=xmltojson.__license__,
    description='',
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
    keywords='xml to json converter',
    include_package_data=True,
    packages=find_packages(),
    py_modules=['xmltojson'],
    scripts=['xmltojson.py']
)
