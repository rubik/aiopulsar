import os
from setuptools import setup


REQUIRES = []
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fobj:
    readme = fobj.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as fobj:
    for line in fobj:
        if not line.startswith(('#', '-e')):
            REQUIRES.append(line)

setup(
    name='aiopulsar',
    version='0.0',
    author='Michele Lacchia',
    author_email='michelelacchia@gmail.com',
    download_url='https://pypi.python.org/aiopulsar/',
    license='MIT',
    description='Async Python client for Apache Pulsar',
    platforms='any',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=REQUIRES,
    keywords='apache pulsar async message queue pub-sub',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Distributed Computing',
    ],
)
