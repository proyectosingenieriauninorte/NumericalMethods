from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="marlonpy",
    version="0.1.1",
    author="Gabriela Bula, Lena Castillo, Edgar Garcia",
    author_email="",
    description="A package for numerical methods in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LCCastillo03/NumericalMethods",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.3',
    install_requires=[
        "numpy",
        "sympy",
        "tabulate",
    ],
)