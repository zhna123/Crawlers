# Automatically created by: shub deploy

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zappos_pkg",
    version="0.0.1",
    author="Na Zhao",
    author_email="cszhna@gmail.com",
    description="zappos scraping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhna123/Crawlers",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
