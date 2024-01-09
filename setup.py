from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name='nAdjPval',
    version='1.0',
    author='Jonathan Gendron',
    author_email='jegendron@gmail.com',
    packages=find_packages(),
    install_requires=[
    ],

    # To automatically import the README into the package
    long_description=description,
    long_description_content_type="text/markdown"
)