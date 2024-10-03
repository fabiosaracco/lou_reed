import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.19',
    author='f4b10',
    description='General purpose package for personal use. Do not code and drive.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/sarawalk/toolbox',
    license='MIT',
    packages=['toolbox'],
    install_request=['numpy', 'datetime', 'igraph', 'tqdm'],
)
