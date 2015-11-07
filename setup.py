#from distutils.core import setup
from setuptools import setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='pullmedown',
    version='0.0.2',
    author='alfateam123',
    author_email='alfateam123@gmail.com',
    packages=['pullmedown'],
    url='http://rigel.tehga.me/gogs/winterthediplomat/pullmedown',
    #license='LICENSE.txt',
    description='downloadin\' all day long',
    long_description=LONG_DESCRIPTION,
    install_requires=[
       "click", "requests", "feedparser"
    ],
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
      'console_scripts': [
        'pullmedown=pullmedown:main'
      ]
    },
    extras_require = {
        #'dev': ['check-manifest'],
        'test': ['pexpect', 'lettuce', 'six'],
    },
    test_suite="tests"
)
