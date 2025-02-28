#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "transformers",
    "datasets",
    "captum",
    "einops",
    "shap",
    "seaborn",
    "matplotlib",
    "scikit-image",
    "lime"
]

test_requirements = []

setup(
    author="Giuseppe Attanasio",
    author_email="giuseppeattanasio6@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    description="A python package for NLP explainability",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="nlxplain",
    name="nlxplain",
    packages=find_packages(include=["nlxplain", "nlxplain.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/g8a9/nlxplain",
    version="0.1.0",
    zip_safe=False,
)
