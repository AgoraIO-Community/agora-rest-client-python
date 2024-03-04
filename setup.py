# coding: utf-8
from os import path
from setuptools import setup, find_packages

NAME = "agora_rest_client"
VERSION = "0.2.0"
AUTHOR = "Agora REST Client"
URL = "https://github.com/AgoraIO-Community/agora-rest-client-python"

DESCRIPTION = "agora rest client"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

OPTIONS = {
    'bdist_wheel': {
        'universal': True
    }
}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["agora", "rest", "client", "agora_rest_client", "agora-rest-client"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements,
    python_requires="!=3.0.*,!=3.1.*,!=3.2.*",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ]
)
