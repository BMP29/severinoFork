from setuptools import setup, find_packages

setup(
    name='severino',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'mypy',
        'pytest',
        'pytest-cov',
        'requests',
        'types-requests',
    ]
)
