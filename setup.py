from setuptools import setup, find_packages
import xmltojson

install_reqs = ['xmltodict']

setup(
    name=xmltojson.__name__,
    version=xmltojson.__version__,
    url=xmltojson.__url__,
    author=xmltojson.__author__,
    author_email=xmltojson.__author_email__,
    license=xmltojson.__license__,
    description=xmltojson.__description_long__,
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
    keywords=xmltojson.__keywords__,
    include_package_data=True,
    install_requires=install_reqs,
    packages=find_packages('.'),
    py_modules=['xmltojson'],
    scripts=['xmltojson.py']
)
