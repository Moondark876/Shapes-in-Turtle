import setuptools


def readme_text():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='Shapes',
    packages=['shapes'],
    version='1.0.0',
    description='Library for Shapes in Python using turtle',
    long_description=readme_text(),
    author='Moondark876',
    url='https://github.com/Moondark876/Shapes-in-Turtle',
    install_requires=['turtle'],
)