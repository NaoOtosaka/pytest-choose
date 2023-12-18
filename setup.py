"""
@File: setup.py
@Author: Azusa
@Description: 

"""
import setuptools

PACKAGE = "pytest-choose"

install_requires = [
    'pytest>=7.0.0'
]

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE,
    version="0.0.6",
    keywords="pytest",
    author="Azusa",
    author_email="naotosaka@126.com",
    description="Provide the pytest with the ability to collect use cases based on rules in text files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/NaoOtosaka/pytest-choose",
    packages=setuptools.find_packages(),
    install_requires=[
        'pytest>=7.0.0',
    ],
    classifiers=[
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Source Code': 'https://github.com/NaoOtosaka/pytest-choose',
        'Bug Tracker': 'https://github.com/NaoOtosaka/pytest-choose/issues',
    },
    entry_points={
        'pytest11': [
            'pytest-choose = pytest_choose.plugin',
        ]
    }
)
