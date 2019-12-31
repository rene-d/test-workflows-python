import sys
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="testpy",
    version="1.0.2",
    description="Blah blah",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rene-d/test-workflows-python",
    author="rene-d",
    author_email="rene.github@gmail.com",
    classifiers=[
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    # keywords="python github",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5",
    # install_requires=["requests"],
    entry_points={"console_scripts": ["testpy=testpy.main:main"]},
    project_urls={
        "Source": "https://github.com/rene-d/test-workflows-python",
        "Bug Reports": "https://github.com/rene-d/test-workflows-python/issues",
    },
)
