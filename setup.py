from setuptools import setup, find_packages


setup(
    name='treestruct',
    version='0.1.0',
    description='Build and manipulate bi-directional tree structures',
    author='Shady Rafehi',
    author_email='shadyrafehi@gmail.com',
    packages=find_packages(),
    install_requires=['graphviz']
)
