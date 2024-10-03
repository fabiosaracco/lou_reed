import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lou_reed',
    version='0.0.1',
    author='fabiosaracco',
    description='LOUvain algorithm with REshufflED node',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fabiosaracco/lou_reed/',
    license='MIT',
    packages=['lou_reed'],
    install_request=['numpy', 'datetime', 'igraph', 'tqdm'],
)
