from setuptools import setup, find_packages

setup(
    name="quick_in_voice",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "fpdf",
        "pandas",
        "reportlab",
        "openpyxl"
    ],
    author="Nathishwar",
    author_email="nathishwarc@gmail.com",
    description="A simple automated invoice generation package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nathishwar-prog/Invoicegenerator_module-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)