# coding: utf-8

"""
    Father Ted API

    REST API for hand-curated Father Ted Quotes  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dave@paddez.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "father-ted-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Father Ted API",
    author_email="dave@paddez.com",
    url="",
    keywords=["Swagger", "Father Ted API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    REST API for hand-curated Father Ted Quotes  # noqa: E501
    """
)
