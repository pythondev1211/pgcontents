from __future__ import print_function
from setuptools import setup, find_packages
from os.path import join, dirname, abspath
import sys


long_description = ''

if 'upload' in sys.argv or '--long-description' in sys.argv:
    with open('README.rst') as f:
        long_description = f.read()


def read_requirements(basename):
    reqs_file = join(dirname(abspath(__file__)), basename)
    with open(reqs_file) as f:
        return [req.strip() for req in f.readlines()]


def main():
    reqs = read_requirements('requirements.txt')
    test_reqs = read_requirements('requirements_test.txt')

    setup(
        name='pgcontents',
        version='0.6',
        description="A Postgres-backed ContentsManager for IPython/Jupyter.",
        long_description=long_description,
        author="Scott Sanderson",
        author_email="ssanderson@quantopian.com",
        packages=find_packages(include='pgcontents.*'),
        license='Apache 2.0',
        include_package_data=True,
        zip_safe=False,
        url="https://github.com/quantopian/pgcontents",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Framework :: IPython',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python',
            'Topic :: Database',
        ],
        install_requires=[
            'SQLAlchemy>=1.0.5',
            'alembic>=0.7.6',
            'click>=3.3',
            'cryptography>=1.4',
            'psycopg2>=2.6.1',
            'six>=1.9.0',
            'notebook>=5.0',
        ],
        extras_require={
            'test': [
                'notebook[test]',
                'nose',
                'nose-ignore-docstring',
                'requests',
                'mock',
            ],
        },
        scripts=[
            'bin/pgcontents',
        ],
    )


if __name__ == '__main__':
    main()
