# coding: utf-8
from setuptools import setup, find_packages
import os


# not so bad: http://joebergantine.com/blog/2015/jul/17/releasing-package-pypi/
version = __import__('svg_tag').__version__


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-svg-tag",
    version=version,
    url='https://github.com/bnzk/django-svg-tag',
    license='MIT Licence',
    platforms=['OS Independent'],
    description="django svg tag",
    long_description=read('PYPI.rst'),
    author=u'Ben Stähli',
    author_email='bnzk@bnzk.ch',
    packages=find_packages(),
    install_requires=(
        'django>=1.8',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)