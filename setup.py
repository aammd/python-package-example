from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/aammd/python-package-example',
    author='Andrew Macdonald',
    author_email='aammacdonald@gmail.com'
)