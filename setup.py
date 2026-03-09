from setuptools import setup, find_packages

setup(
    name="tabata",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "plotly",
        "tables",
        "lxml",
        "scipy",
        "ipywidgets",
        "jupyter"
    ],
)